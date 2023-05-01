import os
from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip 
from pyautogui import press
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution as takeCommand
import pywhatkit as kit
import webbrowser
from time import sleep


def DownloadYtVideos():
    Speak("Tell me the name of the video you want to download")
    VideoName = takeCommand().lower()
    Speak("Downloading "+VideoName)
    try:
        kit.playonyt(VideoName)
        sleep(5)
        hotkey('ctrl','l')
        sleep(1)
        hotkey('ctrl','x')
        sleep(1)
        link = pyperclip.paste()
        YouTube(link).streams.first().download("E\\Users\\user\\Desktop\\Jarvis-2.0\\DataBase\\YtDownloads")
        Speak("Downloaded "+VideoName)
    except Exception as e:
        Speak("Sorry, an error occurred while downloading the video.")
        print(e)



def PlayOnYt(Query):
    Query = str(Query).lower()
    if 'play on youtube' in Query:
            Speak("What should I play")
            song = takeCommand().lower()
            kit.playonyt(f"{song}")
            Speak(f"playing {song} on youtube")


