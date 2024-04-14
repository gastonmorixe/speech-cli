# 
# OpenAI TTS with Streaming
# V1
#
# Author: Gaston Morixe (gaston@gastonmorixe.com)
# Apr 14 2024
#

import time
from pathlib import Path
from time import sleep
import pyaudio
from openai import OpenAI
import sys

# gets OPENAI_API_KEY from your environment variables
openai = OpenAI()

def stream_to_speakers() -> None:
    player_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)

    start_time = time.time()

    input_string = sys.stdin.read()

    with openai.audio.speech.with_streaming_response.create(
        model="tts-1-hd",
        voice="alloy",
        response_format="pcm",  # similar to WAV, but without a header chunk at the start.
        input=input_string,
    ) as response:
        print(f"Time to first byte: {int((time.time() - start_time) * 1000)}ms")
        for chunk in response.iter_bytes(chunk_size=1024):
            player_stream.write(chunk)
          
        # prevents end glitch at playback
        sleep(1) 
        
    print(f"Done in {int((time.time() - start_time) * 1000)}ms.")

def main() -> None:
    stream_to_speakers()

if __name__ == "__main__":
    main()

# TODO: 
# - [ ] Chunk longer texts in smaller parts
# - [ ] Store raw input text
# - [ ] Store output (cache?) in a better place
# - [ ] Command line cli
# - [ ] Command line accept arguments for all params instead of hardcoded
# - [ ] Offer some sort of cache give the same or similar input (so it's less expensive in compute and $$)
# - [ ] Global shortcut (for mac at least) or guide for this
# - [ ] Configuration file
# - [ ] Option to see the text in real time highlighted
# - [ ] Option to see the estimated price and processing upfront
