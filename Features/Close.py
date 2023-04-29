import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def CloseExe(Query):
    Query = str(Query).lower()

# code to close the application

    if "close" in Query:
        pyautogui.press('alt')
        sleep(0.5)
        pyautogui.press('f4')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(0.5)
        return True


    # elif "start" in Query:
    #     Nameoftheapp = Query.replace("open ","")

    #     if "chrome" in Nameoftheapp:
    #         os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    #         return True
