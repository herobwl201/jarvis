import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from YT_auto import *
from News import *
import randfacts
from jokes import *
from weather import *
import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return("morning")
    elif hour >= 12 and hour < 6:
        return("afternoon")
    else:
        return("evening")


today_date = datetime.datetime.now()

r = sr.Recognizer() # Retrieve recognition from a source (Microphone)

speak("hello sir, good "+wishme()+ ", i'm JARVIS.")
speak("How are you feeling?")

with sr.Microphone() as source:
        r.energy_threshold = 10000 # energy_threshold does increase spetch of phone voice
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
    
if "what" and "about" and "you" in text:
    speak("I am also having a good day sir. How can I help you?")
    

while True:
    with sr.Microphone() as source:
        r.energy_threshold = 10000 
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)
    
    if "information" in text2:
        speak("you need information related to which topic?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000 
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            infor = r.recognize_google(audio)

        assist = infow()
        info_text = assist.get_info(infor)
        print(info_text)
        speak(info_text)
    
    elif "play" in text2 and "video" in text2:
        speak("you want me to play which video?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000 
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
            print("Playing {} on Youtube".format(vid))
            assist = music()
            assist.play(vid)

    elif "news" in text2:
        print("Sure sir. Now I will read news for you.")
        speak("Sure sir. Now I will read news for you.")
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif "joke" in text2 or "jokes" in text2:
        speak("sure sir, get ready for some chuckles")
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])

    elif "fact" in text2 or "facts" in text2:
        speak("Sure sir, ")
        x = randfacts.get_fact()
        print(x)
        speak("Did you know that," + x)

    elif "weather" in text2.lower():
        temperature, description = get_weather()
        print(temperature, description)
        speak(f"Temperature in Vietnam is {temperature} degree Celsius and with {description}")
    
    speak("What's now, sir?")