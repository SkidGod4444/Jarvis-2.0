from pyautogui import click
from pyautogui import hotkey
import pyperclip 
import os
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution as takeCommand
import keyboard as kb
import pyautogui



def InstaReelsScroller():
    pyautogui.press('win')
    sleep(1)
    kb.write('Instagram')
    sleep(1)
    kb.press('enter')
    sleep(0.5)
    click(x=139,y=502)
    sleep(2)
    click(x=1280,y=137)
    for x in range(50000):
        sleep(60)
        kb.press('down')
        if 'stop scrolling' in takeCommand():
            break
            Speak("Stopped")
        else:
            pass


def InstaReelsMute():
    sleep(1)
    click(x=1280,y=137)
    Speak("Muted")

def InstaReelsUnmute():
    sleep(1)
    click(x=1280,y=137)
    Speak("Unmuted")

def InstaReelsLike():
    sleep(1)
    click(x=1389,y=496)
    Speak("Liked!")

def InstaReelsComment():
    sleep(1)
    click(x=1385,y=613)
    sleep(2)
    Speak("What should I comment?")
    Comment = takeCommand()
    sleep(1)
    kb.write(Comment)
    sleep(1)
    kb.press('enter')
    Speak("Commented!")

def InstaReelsShare():
    sleep(1)
    click(x=1394,y=695)
    sleep(2)
    Speak("Whom should I share? tell me the username")
    Comment = takeCommand()
    sleep(1)
    kb.write(Comment)
    sleep(1)
    kb.press('tab')
    sleep(1)
    kb.press('enter')
    Speak("Shared!")

def InstaReelsPause():
    sleep(1)
    click(x=1084,y=528)
    Speak("Paused!")
    
def InstaReelsPlay():
    sleep(1)
    click(x=1084,y=528)
    Speak("Playing!")

def InstaReelsNext():
    sleep(1)
    kb.press('down')
    Speak("Next!")

def InstaReelsPrevious():
    sleep(1)
    kb.press('up')
    Speak("Previous!")



