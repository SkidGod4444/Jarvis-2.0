from pyautogui import click
from pyautogui import hotkey
import pyperclip 
import os
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution as takeCommand
import keyboard as kb
import pyautogui

def YoutubeSearch():
    pyautogui.press('win')
    sleep(1)
    kb.write('YouTube')
    sleep(1)
    kb.press('enter')
    sleep(1)
    Speak("What should I search?")
    Search = takeCommand()
    sleep(1)
    click(x=631,y=102)
    sleep(0.5)
    kb.write(Search)
    sleep(1)
    kb.press('enter')
    Speak("Searching" + Search)

def YoutubeAutoPause():
    kb.press('space bar')
    Speak("Paused the yt video")

def YoutubeAutoPlay():
    kb.press('space bar')
    Speak("Playing the yt video")

def YoutubeAutoMute():
    kb.press('m')
    Speak("Muted the yt video")

def YoutubeAutoUnmute():
    kb.press('m')
    Speak("Unmuted the yt video")

def YoutubeAutoLike():
    kb.press('l')
    Speak("Liked the yt video")

def YoutubeAutoDislike():
    kb.press('d')
    Speak("Disliked the yt video")  

def YoutubeAutoNext():
    kb.press('n')
    Speak("Playing next video")

def YoutubeAutoPrevious():
    kb.press('p')
    Speak("Playing previous video")

def YoutubeAutoSkip():
    kb.press('right')
    Speak("Skipping 5 seconds")

def YoutubeAutoBack():
    kb.press('left')
    Speak("Going back 5 seconds")

def YoutubeAutoFullScreen():
    kb.press('f')
    Speak("Full Screen Mode")

def YoutubeAutoExitFullScreen():
    kb.press('esc')
    Speak("Exit Full Screen Mode")

def YoutubeAutoTheatreMode():
    kb.press('t')
    Speak("Theatre Mode")   

def YoutubeAutoExitTheatreMode():
    kb.press('t')
    Speak("Exit Theatre Mode")

def YoutubeAutoMiniPlayer():
    kb.press('i')
    Speak("Mini Player Mode")

def YoutubeAutoExitMiniPlayer():
    kb.press('i')
    Speak("Exit Mini Player Mode")

def YoutubeAutoSettings():
    kb.press('tab')
    kb.press('tab')
    kb.press('tab')
    kb.press('tab')
    kb.press('tab')
    kb.press('tab')
    kb.press('tab')
    kb.press('tab')
    kb.press('tab')
    kb.press('enter')
    Speak("Opened Settings")

def YoutubeAutoExitSettings():
    kb.press('esc')
    Speak("Exit Settings")

def YoutubeAutoSpeedInc():
    kb.press('shift' + '.')
    Speak("Speed Increased")

def YoutubeAutoSpeedDec():
    kb.press('shift' + ',')
    Speak("Speed Decreased")

def YoutubeAutoSpeedNormal():
    kb.press('shift' + 'n')
    Speak("Speed Normal")







