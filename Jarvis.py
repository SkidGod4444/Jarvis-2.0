from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print("-->> Importing Modules")
from Body.Speak import Speak
from Features.Clap import Tester
print("-->> Importing Jarvis-2.0")
from Main import MainTaskExecution
from time import sleep
from Body.Listen import MicExecution as TakeCommand
def MainExecution():
    sleep(1)
    print("-->> Started The Jarvis : Wait For Few Seconds More")
    Speak("Hello dude I am Jarvis")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass


        elif "download this video" in Data:
            from Features.Extra import DownloadYtVideos
            Value = DownloadYtVideos()
            return Value
        # elif "whatsapp message" in Data:
        #     pass

        # elif "turn on the tv" in Data:# Specific COmmand
        #     Speak("Ok..Turning On The Android TV")
        elif "nasa news" in Data or "space news" in Data:
            sleep(1)
            Speak("Please input the date (YYYY-MM-DD)!")
            Date = input()
            from Features.Nasa import NasaNews
            try:
                NasaNews(Date)
            except Exception as e:
                sleep(1)
                Speak("Sorry, an error occurred while retrieving NASA news.")
                print(e)


        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        else:
            Reply = ReplyBrain(Data)
            sleep(1)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

