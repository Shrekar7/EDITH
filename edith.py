from ast import Try
import imp
from multiprocessing.pool import TERMINATE
from time import struct_time
from tkinter import Place
from tkinter.messagebox import YES
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import subprocess
from os import startfile
from time import sleep
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder  
from pyautogui import click
from keyboard import press
from keyboard import write
import cv2
import numpy as np
import requests
import pyautogui as p


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("i am edith,how can i help you")
def open_chrome():
    url = "https://www.google.co.in/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
def GoogleMaps(place):
    

    url_place = "https://www.google.com/maps/place" + str(place)
    
    geolocator =  Nominatim(user_agent = "myGeocoder")

    location = geolocator.geocode(place, addressdetails=True)
    
    target_lation = (geolocator.latitude , geolocator.longitude)
    print(target_lation)
    
    webbrowser.open(url = url_place)
 
    location = location.raw['address']
    
    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_location = geocoder.ip('me')

    current_latlon = current_location.latlng

    distance = str(great_circle(current_latlon,target_lation))
    distance = str(distance.split('',1)[0])
    distance = round(float(distance),2)

    webbrowser.open(url=url_place) 
    speak(target)
    speak(f"sir,{place} is {distance} kilometers away from your location")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query
if __name__ == "__main__":


 def TaskExecution():
    speak("verification successful")
    speak("welcome back Master Srikar")
    wishMe()
    p.press('esc')
    cam.release()
     
    while True: 
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            queary = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'hello' in query:
            speak('hello sir how can i help you')

        elif 'who are you' in query:
            speak('I am an voice assistant , how may i help you')
            

        elif 'play music' in query:
            music_dir = 'C:\\Users\\shrekar reddy\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%m:%S")
            speak(f"Sir!, the time is {strTime}")
            print(strTime) 

        elif 'open vscode' in query:
            
             codePath = "C:\\Users\\shrekar reddy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)
        
        elif 'close vscode' in query:
            speak("closing vscode")
            codePath.terminate()
        
        elif 'open notepad' in query:
            speak("opening notepad")
            location = "C:/Windows/notepad.exe"
            notepad = subprocess.Popen(location)

        elif 'close notepad' in query:
            speak("closing notepad")
            notepad.terminate()
        
        elif 'open chrome' in query:
            open_chrome()

        elif 'close chrome' in query:
            open_chrome.terminate()

        elif 'search' in query:
            speak("what should i search?")
            search = takeCommand().lower()
            speak('opening' + search)
            webbrowser.get(chrome_path).open_new_tab(search + ".com") 

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.get(chrome_path).open_new_tab("https://www.youtube.com/") 


        elif 'open whatsapp' in query:
            speak('opening whatsapp')
            webbrowser.get(chrome_path).open_new_tab('https://web.whatsapp.com/')

        elif 'shutdown' in query:
            speak("shutting out in 5 seconds")
            sleep(5)
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("restarting out in 5 seconds")
            sleep(5)
            os.system("shutdown /r /t 1")

        elif 'where is' in query:
            
            place = query.replace("where is","")
            place = query.replace("edith","")
            GoogleMaps(place)
        
        elif 'i love you' in query:
            speak('sorry i am already in relation with wifi')
            
        elif 'whatsapp message' in query:
            name = query.replace("send whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            speak("what is the Message for " + Name)
            MSG = takeCommand()
            from test import whatsappMsg
            whatsappMsg(Name, MSG)

        elif 'call' in query:
            from test import whatsappcall
            name = query.replace("call","")
            Name = str(name)
            whatsappcall(Name)

        elif 'show chat' in query:
            speak("with whom?") 
            name = takeCommand()
            from test import whatsappchat
            whatsappchat(name)
        
        elif 'record' in query:
            speak("recording started")
            import recorder
        
        elif 'exit' in query:
            speak("here to help in any time sir")
            os._exit(0)


#its just a code that we have imported for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "C:\\Users\\shrekar reddy\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 2

names=['','avi']

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
         )
    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

        if (accuracy < 50):
            id = names[id]
            accuracy = " {0}%".format(round(100 - accuracy))
            TaskExecution()

        else:
            id = "unknown"
            accuracy = " {0}%".format(round(100 - accuracy))
            speak('access denined')
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255),2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0),1)

    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff
    if k==27:
        break
print("thanks for using this program, have a good day")
cam.release()
cv2.destroyAllWindows()


            
