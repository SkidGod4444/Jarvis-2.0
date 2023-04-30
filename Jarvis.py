from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
from Main import MainTaskExecution
from Body.Listen import MicExecution as TakeCommand
print(">> Started The Jarvis : Wait For Few Seconds More")
def MainExecution():
    Speak("Hello Sir I am Jarvis, Your Personal Assistant. How May I Help You?")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        # elif "whatsapp message" in Data:
        #     pass

        # elif "turn on the tv" in Data:# Specific COmmand
        #     Speak("Ok..Turning On The Android TV")
        elif "nasa news" in Data or "space news" in Data:
            Speak("Tell me the date pls!")
            Date = TakeCommand()
            from Features.Converter import DateConvt
            Value = DateConvt(Date)
            from Features.Nasa import NasaNews
            NasaNews(Value)

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

