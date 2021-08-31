# text to speech
import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)
engine.say("Hello sir")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("How can I help you")

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    monthNumber = int(datetime.datetime.now().month)
    if (monthNumber == 8):
        month = "August"
    day = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(day)
    speak(month)
    speak(year)
date()
