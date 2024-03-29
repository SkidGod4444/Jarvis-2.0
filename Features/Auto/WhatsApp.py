from pyautogui import click
from pyautogui import hotkey
import pyperclip 
import os
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution as takeCommand
import keyboard as kb
import pyautogui

def WhatsAppAutoMsg():
    pyautogui.press('win')
    sleep(1)
    kb.write('WhatsApp')
    sleep(1)
    kb.press('enter')
    sleep(2)
    Speak("Whom you want me to msg?")
    Name = takeCommand()
    sleep(1)
    kb.press('ctrl' + 'f')
    sleep(0.5)
    kb.write(Name)
    sleep(1)
    Speak("Found ?" + Name)
    kb.press('down')
    sleep(1)
    kb.press('enter')
    sleep(1)
    Speak("What should I send?")
    Msg = takeCommand()
    sleep(1)
    kb.write(Msg)
    sleep(1)
    kb.press('enter')
    Speak("Message sent!")

def WhatsAppAutoReply():
    Speak("Whom you want me to reply?")
    Name = takeCommand()
    sleep(1)
    kb.press('ctrl' + 'f')
    sleep(0.5)
    kb.write(Name)
    sleep(1)
    Speak("Found ?" + Name)
    kb.press('down')
    sleep(1)
    kb.press('enter')
    sleep(1)
    Speak("Wait for 5 seconds")
    sleep(0.5)
    kb.write("Hey, I am *Jarvis* .My boss is busy right now. He will reply you later. I have informed him about your message. Thank you!")
    sleep(1)
    kb.press('enter')
    Speak("Auto Message sent!")

def WhatsAppCall():
    pyautogui.press('win')
    sleep(1)
    kb.write('WhatsApp')
    sleep(1)
    kb.press('enter')
    sleep(2)
    Speak("Whom you want me to call?")
    Name = takeCommand()
    sleep(1)
    kb.press('ctrl' + 'f')
    sleep(0.5)
    kb.write(Name)
    sleep(1)
    Speak("Found ?" + Name)
    kb.press('down')
    sleep(1)
    kb.press('enter')
    sleep(1)
    click(x=1485, y=163)
    sleep(1)
    Speak("Calling!")

def WhatsAppVideoCall():
    pyautogui.press('win')
    sleep(1)
    kb.write('WhatsApp')
    sleep(1)
    kb.press('enter')
    sleep(2)
    Speak("Whom you want me to call?")
    Name = takeCommand()
    sleep(1)
    kb.press('ctrl' + 'f')
    sleep(0.5)
    kb.write(Name)
    sleep(1)
    Speak("Found ?" + Name)
    kb.press('down')
    sleep(1)
    kb.press('enter')
    sleep(1)
    click(x=1424, y=161)
    sleep(1)
    Speak("Calling!")

