
import pyttsx3 as p
import speech_recognition as sr
import webbrowser
import wikipedia as w
import datetime as d
import os
import pyaudio





def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing..")
            response = r.recognize_google(audio, language='en-in')
            print(f"Your request is: {response}\n")
            return response
        except Exception as e:
            print(e)
            print("Say again please...")
            return "None"
      

def speak(audio):
    engine = p.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def tell_datetime():
    hour = int(d.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning..!")
    elif 12 <= hour < 18:
        speak("Good Afternoon..!")
    else:
        speak("Good Evening..!")


def hello():
    speak("Hello.. I am your desktop assistant How could I help you..")


def take_queries():
    hello()
    while(True):
        query = take_command().lower()
        if 'open twitter' in query:
            speak("Opening twitter")
            webbrowser.open("www.twitter.com")
                
            
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
        elif 'what is the time' in query:
            Time = d.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{Time}")

        elif 'open PyCharm' in query:
            Path = "/Applications/PyCharmCE.app"
            os.startfile(Path)

            
    

        
if __name__ == '__main__':
    tell_datetime()
    take_queries()
    
        
    
