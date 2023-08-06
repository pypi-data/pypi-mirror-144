import asyncio
import json
import logging
import websockets
import base64
import sys
import re
import threading
from google.cloud import speech
from six.moves import queue

logging.basicConfig(level=logging.INFO)

BUFFER_COUNT = 5 # to add up audio segments to 100ms as recommended by Google

def listen_print_loop(responses):
    """Iterates through server responses and prints them.
    The responses passed is a generator that will block until a response
        is provided by the server.
    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
        print only the transcription for the top alternative of the top result.
    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        if not response.results:
                continue
        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
                continue
        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript
        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = " " * (num_chars_printed - len(transcript))
        if not result.is_final:
            sys.stdout.write(f'{transcript}{overwrite_chars}\r')
            sys.stdout.flush()
            num_chars_printed = len(transcript)
        else:
            print(transcript + overwrite_chars)
            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break
            num_chars_printed = 0

class Transcoder(object):
    """
    Converts audio chunks to text
    """
    def __init__(self):
        self.buff = queue.Queue()
        self.closed = False
        self.transcript = None
        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MULAW,
            sample_rate_hertz=8000,
            language_code="en-US",
            max_alternatives=1,
            model='phone_call'
            )
        self.streaming_config = speech.StreamingRecognitionConfig(   
            config=self.config, interim_results=True,
        )
        """Start up streaming speech call"""
        t = threading.Thread(target=self.process)
        t.isDaemon = True
        t.start()

    
    def process(self):
        """
        Audio stream recognition and result parsing
        """
        audio_generator = self.stream_generator()
        requests = (speech.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = self.client.streaming_recognize(self.streaming_config, requests)
        listen_print_loop(responses)

    def stream_generator(self):
        while not self.closed:
            chunk = self.buff.get()
            if chunk is None:
                return
            data = [chunk]
            while True:
                try:
                    chunk = self.buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break
            yield b''.join(data)

    def write(self, data):
        """
        Writes data to the buffer
        """
        self.buff.put(data)
    
    def exit(self):
        self.closed = True

def log_message(message: str) -> None:
    logging.info(f"Message: {message}")

async def handle(websocket, path):
    logging.info(path) 
    transcoder = Transcoder()
    buffer_counter=0
    buffer = b""
    async for messageStr in websocket:
        # logging.info(messageStr)
        message = json.loads(messageStr)
        if message["event"] is not None and message["event"] == "Connected":
            logging.info("Consumed ACK")
        elif message["event"] is not None and message["event"] == "Start":
            print("start")
        elif message["event"] is not None and message["event"] == "Media":
            buffer_counter += 1
            media = message["media"]
            media_bytes = base64.b64decode(media)
            if buffer_counter > BUFFER_COUNT:
                transcoder.write(buffer)
                buffer_counter=0
                buffer = b""
            else:
                buffer = buffer + media_bytes
        elif message["event"] is not None and message["event"] == "Stop":
            transcoder.exit()
            break

async def main(port):
    async with websockets.serve(handle, '127.0.0.1', port, ping_interval=1, ping_timeout=500000):
        await asyncio.Future()  # run forever
