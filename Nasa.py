fileopen = open("Data\\NasaApi.txt","r")
API = fileopen.read()
fileopen.close()

# Importing
import requests
import os
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution as TakeCommand


#Coding
Api_Key = API

def NasaNews(Date):
    
    Api_Url = "https://api.nasa.gov/planetary/apod?api_key="+str(Api_Key)
    Params = {'date':str(Date)}
    Response = requests.get(Api_Url,params=Params)
    Data = Response.json()

# Extraction
    Info = Data['explanation']
    Title = Data['title']
    Image = Data['url']
    
    Image_response = requests.get(Image)
    FileName = str(Date)+".jpg"
    with open("DataBase\\Nasa\\"+str(FileName),"wb") as file:
        file.write(Image_response.content)

    

    Speak("Title : "+str(Title))
    Speak("According to my data : "+str(Info))
    Speak("Do you want to read more about it ?")
    Answer = TakeCommand()
    if "yes" in Answer:
        Speak("Opening Browser")
        os.startfile(Data['hdurl'])
    else:
        Speak("Okay")
        sleep(1)
    Speak("Do you want to see the image ?")
    Answer = TakeCommand()
    if "yes" in Answer:
        os.startfile("DataBase\\Nasa\\"+str(FileName))
    else:
        Speak("Okay")