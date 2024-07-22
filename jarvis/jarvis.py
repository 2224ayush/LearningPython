import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import setuptools
import wikipedia
import pyaudio
import os
from appopener_test import open
from bs4 import BeautifulSoup
import requests
engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning Master")
    elif 12<=hour<5:
        speak("Good Afternoon Master")
    else:
        speak("Good evening master")
    speak("I am jarvis sir , how may i assist you today")
def command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        print("Listening...")
        r.pause_threshold =1
        r.energy_threshold=300
        audio=r.listen(source,timeout=6)
    try:
        speak("recognizing...")
        print("recognizing...")
        query=r.recognize_google(audio)
        print("Master said",query)
    except Exception as e:
        print(e)
        speak("Master could you please repeat?")
        print("Master could you please repeat?")
        return "None"
    return query
def command1():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        r1.pause_threshold = 1
        r1.energy_threshold = 300
        audio = r1.listen(source, timeout=6)

if __name__=="__main__":
    speak("Initializing Jarvis...")
    wishme()
    ans="yes"
    while True:
        query = command().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            print("searching wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print("according to wikipedia")
            speak(result)
        elif "youtube" in query:
            print("opening youtube...")
            speak("opening youtube")
            query=query.replace("open youtube","")
            webbrowser.open("www.youtube.com")
        elif "favourite music" in query:
            print("playing your favourite sound on youtube sir.")
            speak("playing your favourite sound on youtube sir.")
            query = query.replace("favourite sound", "")
            webbrowser.open("https://www.youtube.com/watch?v=d2LePn83P7s")
        elif "motivation" in query:
            print("playing a video by andrew tate sir...")
            speak("playing a video by andrew tate sir...")
            query=query.replace("motivation","")
            webbrowser.open("https://www.youtube.com/watch?v=T9X8cuACyf8")
        elif "instagram" in query:
            print("opening instagram sir...")
            speak("opening instagram sir")
            query = query.replace("instagram", "")
            webbrowser.open("www.instagram.com")
        elif "whatsapp" in query:
            print("opening whatsapp")
            speak("opening whatsapp")
            query = query.replace("whatsapp", "")
            open("WhatsApp")
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M")
            print(f"sir the time is {strtime}")
            speak(f"sir the time is {strtime}")
        elif "temperature" in query:
            print("showing results via accuweather...")
            speak("showing results via accuweather...")
            query = query.replace("temperature", "")
            webbrowser.open("https://www.accuweather.com/en/in/champawat/201492/current-weather/201492")
        elif "shutdown" in query:
            print("have a good time sir")
            speak("have a good time sir")
            query = query.replace("shutdown", "")
            os.system("shutdown -s")
        elif "stop jarvis" in query:
            speak("see you soon sir")
            print("see you soon sir...")
            break
        speak("anything else master:")
