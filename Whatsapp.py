# from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
# from time import sleep
# from selenium import webdriver
# import pandas as pd
# from Body.Speak import Speak
# import pathlib
# from Body.Listen import MicExecution

# scriptDirectory = pathlib.Path().absolute()

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"
# PathofDriver = "DataBase\\chromedriver.exe"
# driver = webdriver.Chrome(PathofDriver,options=options)
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# Speak("Initializing The Whatsapp Software.")

# ListWeb = {'dhruv' : "+917011024588",
#             'dost': "+91",
#             "pote": '+91'}

# def WhatsappSender(Name):
#     Speak(f"Preparing To Send a Message To {Name}")
#     Speak("What's The Message By The Way?")
#     Message = MicExecution()
#     Number = ListWeb[Name]
#     LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
#     driver.get(LinkWeb)
#     sleep(5)
#     try:
#         driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
#         Speak("Message Sent")
        
#     except:
#         print("Invalid Number")

