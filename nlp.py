import pyttsx3 as p
import speech_recognition as sr
import spacy
import time

def speak(text):
    engine = p.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Chuyển audio thành văn bản bằng Google API Engine
    text = r.recognize_google(audio)

    print(text)

    # Tải mô hình từ điển tiếng Anh
    nlp = spacy.load("en_core_web_sm")

    # Sử dụng spaCy để phân tích cú pháp câu truy vấn từ người dùng (sử dụng biến 'text' thay vì 'user_query')
    doc = nlp(text)

    # Xác định xem từ khóa "hello" có trong câu truy vấn hay không
    contains_hello = any(token.text.lower() == "hello" for token in doc)

    # Phản ứng dựa trên kết quả
    if contains_hello:
        response = "Hi. How can I help you, sir?"
    else:
        response = "Sorry, can you repeat that?"

    print(response)
    speak(response)

