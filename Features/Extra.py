import os
import time
from Body.Speak import Speak
from Body.Listen import MicExecution as takeCommand
import pywhatkit as kit
import webbrowser
from time import sleep

def PlayOnYt(Query):
    Query = str(Query).lower()
    if 'play on youtube' in Query:
            Speak("What should I play")
            song = takeCommand().lower()
            kit.playonyt(f"{song}")
            Speak(f"playing {song} on youtube")