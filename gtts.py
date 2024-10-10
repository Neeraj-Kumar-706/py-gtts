#google
import subprocess
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

def tts(text):
    subprocess.run(['gtts-cli', text, '--output', 'output.mp3'], check=True, stdout=subprocess.DEVNULL)
    #sleep(1)
    try:
        audio = AudioSegment.from_file("output.mp3")
        play(audio)
    except Exception as e:
        print(f"Error playing audio: {e}")
#tts('hello. hi, sir how are you. my name is shreya')
