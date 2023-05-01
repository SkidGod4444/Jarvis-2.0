import os
import keyboard
from pyautogui import click
import webbrowser
from time import sleep

def CloseExe(Query):
    Query = str(Query).lower()

# code to close the application

    if "close this window" in Query:
        click(x=1887,y=24)
        return True
    


    # elif "start" in Query:
    #     Nameoftheapp = Query.replace("open ","")

    #     if "chrome" in Nameoftheapp:
    #         os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    #         return True
