from pyautogui import click
from pyautogui import hotkey
import pyperclip 
import os
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution as takeCommand
import keyboard as kb
import pyautogui

def InstallApp():
    pyautogui.press('win')
    sleep(1)
    kb.write('Microsoft Store')
    sleep(1)
    kb.press('enter')
    sleep(5)
    click(x=773,y=80)
    sleep(2)
    click(x=800,y=38)
    sleep(1)
    Speak("What app do you want to install?")
    AppName = takeCommand()
    sleep(1)
    kb.write(AppName)
    sleep(1)
    kb.press('enter')
    sleep(1)
    click(x=558,y=344)
    sleep(1)
    click(x=831,y=755)
    sleep(1)
    Speak("App installing!")

