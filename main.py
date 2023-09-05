import venv
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

speak("hello sir, good "+wishme()+ ", i'm your voice assistant.")
speak("today is" + today_date.strftime("%d") + " of" + today_date.strftime("%B") + " And its currently " + today_date.strftime('%Y'))
speak("Temperature in viet nam is" + str(temp()) +" degree celcius" + " and with " + str(des()))
speak("what can i do for you")

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

elif "news" in text2:
    print("Sure sir. Now I will read news for you.")
    speak("Sure sir. Now I will read news for you.")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure sir, ")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that," + x)

elif "joke" or "jokes" in text2:
    speak("sure sir, get ready for some chuckles")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
