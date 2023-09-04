import venv
import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from YT_auto import *


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # Retrieve recognition from a source (Microphone)

speak("hello sir, i'm your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000 # energy_threshold does increase spetch of phone voice
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio) # this line of code does it convert audio and send audio to Google API Engine and Google API Engine convert our audio to context
    print(text)
if "what" and "about" and "you" in text:
    speak("I am also having a good day sir")
speak("what can i do for you?")

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
        infor = r.recognize_google(audio)  # Cập nhật giá trị của biến infor từ giọng nói của người dùng

    assist = infow()
    info_text = assist.get_info(infor)
    print(info_text)
    speak(info_text)
    
elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000 
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)  # Cập nhật giá trị của biến infor từ giọng nói của người dùng
        print("Playing {} on Youtube".format(vid))
        assist = music()
        assist.play(vid)
