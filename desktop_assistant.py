import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio 
import wikipedia
import webbrowser
from googlesearch import search
from AppOpener import open
import datetime
import pyjokes 
import os 
import random
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    pass

def Wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<=17:
        speak("Good afternoon")
    elif hour>17 and hour<=24:
        speak("Good evening") 
    speak(f"{Wishme} Hi sir! I am Alex. How can I help you")
def Username():
    pass

def takeCommand():
    '''If it is showing some error the try to turn ON and OFF you microphone of laptop or mobile. 
    If it is showing again the error then please '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        print("Say that again please...")    
        return "None" 
    return query
def ask(text):
    speak("What time you want to get remainder")
def timer(x):
    
    while x:
        mins, secs = divmod(x, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        x -=1
    
        print('Timer completed! ')

    x= input("Enter time in second ")

    timer(int(x))

def dateandtime(t):
    t=time.localtime()
    return time.asctime([t])

time_phrase= ["what is the time", 'what date is today ','which day is today','today' ]
reminders_phrase =  ['set a reminder', 'remind me ', 'remind me latter', 'remind me this twomorrow ', 'remember this for me']

    
 
if __name__ == '__main__':
    reminders = []
    Wishme()
    while True:
        query=takeCommand().lower()
    #logic for task execution
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Account to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")
        elif 'play music' in query:
            speak("Opening music player")
            open('spotify')
        elif 'set a reminder' in query:
            speak('what is should I remind you sir' )
            new_query=takeCommand()
            reminders.append(new_query)
        elif 'open stack overflow' in query:
            speak('opening it')
            webbrowser.open('https://stackoverflow.com')
        elif 'open chrome' in query:
            speak("opening chrome")
            open('google chrome')    
        elif 'tell me a joke' in query:
            x_1 = (random.choice(pyjokes.get_jokes(language="en",category="all")))
            print(x_1)
            speak(x_1)
        
        elif 'set a timer ' in query:
            speak("How long ")
        
            #speak(f"Setting timer of {x} sec")
        #for phrase in reminders_phrase:
        #    if phrase in query:
         #       file1= open('reminders.txt', 'w')
          #      speak('what do you want me to reminde you about')
           #  rerrt   s=takeCommand()
           #     s_1=str(s)
            #    file1.write(s_1)
             #   file1.close()
             #   speak('I have saved it to reminders')
        for i in time_phrase:
            if i in query:
                t= time.localtime()
                t_1 = time.asctime(t)
                print(t_1)
                speak(t_1)        
               
