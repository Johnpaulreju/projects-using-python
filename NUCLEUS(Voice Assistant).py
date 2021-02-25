import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import datetime
import wikipedia
import webbrowser
import os
import random
import json
import requests
import subprocess
import pyjokes
import smtplib
from urllib.request import urlopen 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#import pyttsx3
#engine that convert text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voices',voices[2].id)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('johnpaul.19bcan039@jecrcu.edu.in', '19bcan039')
    server.sendmail('johnpaul.19bcan039@jecrcu.edu.in', to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("hello")
    speak(uname)
    speak("I am Your assistant")
uname =("john")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=0 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak(" I am nucleus!  Speed 1 terahertz!  memory 1 zeta byte.! How Can I Help you Sir")
    #speak("created by john")
    
def takeCommand():    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")         
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

assname = ("nucleus") 

if __name__ == "__main__":
    
    wishMe()
    username()
    while True:
    #if 2:
        query = takeCommand().lower() 

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'play music' in query:
            n = random.randint(0,6)
            speak('Playing music...')
            music_dir = 'C:\\Users\\p c m\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif  'youtube' in query:
            speak('searching in youtube...')
            query= query.replace("youtube", "")
            kit.playonyt("" + query)

        elif  'fine' in query or "good" in query:
            speak('Thats great sir') 

        elif  'volume' in query:
            speak('Sir! Do you want to increase or decrease the volume')
            query = takeCommand()
            if 'increase' in query or 'raise' in query:
                volume.SetMasterVolumeLevel(-0.0, None) #max volume
                speak("volume has been increased to max level sir!")
                speak("is that ok for you")
                query = takeCommand()
                if 'yes' in query or 'ya' in query or 'fine' in query or 'great' in query:
                    speak("ok sir!")
                elif 'no' in query or 'not that much' in query or 'nope' in query or 'decrease little bit' in query:
                    speak("volume has been decreased to 90 percent sir")
                    volume.SetMasterVolumeLevel(-2.0, None) #90% volume
                elif 'increase little bit' in query:
                    speak("sorry sir! volume can't be further increase")
                else:
                    speak("sir i'm not able to hear you so i'm not changing the volume further")
            elif 'decrease' in query or 'lower' in query:
                volume.SetMasterVolumeLevel(-12.0, None) #45% volume
                speak("volume has been decreased to 45 precent sir!")
                speak("is that ok for you")
                query = takeCommand()
                if 'yes' in query or 'ya' in query or 'fine' in query or 'great' in query:
                    speak("ok sir!")
                elif 'no' in query or 'not that much' in query or 'nope' in query or 'increase little bit' in query:
                    volume.SetMasterVolumeLevel(-8.0, None) #59% volume
                    speak("volume has been increased to 59 precent sir!")
                elif 'decrease little bit' in query:
                    
                    speak("sorry sir! volume cannot be decrease more than this level")
                else:
                    speak("sir i'm not able to hear you so i'm not changing the volume further")
            else:
                pass

        elif 'hello' in query or "hi" in query or "hey" in query or "hai" in query:
            speak('how are you')

        elif 'email' in query:
            try:
                speak("Whom do you want to send Email sir")
                e_person = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                to = (""+e_person)    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
        
        elif "weather" in query:
            api_key="1b2498d6cf39c59086eb63888e86fce7"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                R = (y["temp"]) - 273.15
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n Temperature in Celsius unit is " +
                      str(R) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description is " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n Temperature in Celsius unit is " +
                      str(R) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
    
        elif "news" in query:
            try:
                url = ('https://newsapi.org/v2/top-headlines?''sources=bbc-news&''apiKey=968f006f678f4ae393ec3a3b04014ad7')
                response = requests.get(url)
                text = response.text
                my_json = json.loads(text)
                for i in range(0, 6):
                    speak(my_json['articles'][i]['title'] )
                    print(my_json['articles'][i]['title'] )
            except Exception as e:                 
                print(str(e))

        elif 'message' in query:
            speak("you have to open the chrome to send message! Should i open the chrome for you")
            query = takeCommand()
            if "yes" in query or "yeah" in query or "open" in query:
                webbrowser.get(chrome_path).open("www.google.com" )
                speak("do you want to send someone individual or a group")
                query = takeCommand()
                if "individual" in query:
                    try:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak("whom do u want to send the message! tell me the number sir")
                        phno = takeCommand()
                        speak("what do you want me to send ")
                        message = takeCommand()
                        kit.sendwhatmsg("+91" +phno, "" +message,11,39 )
                        speak("message has been sent")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this message")  
                #elif "group" in query:
                    #try:
                        #speak("which group do u want me to send the message sir")
                        #group = takeCommand()
                        #speak("what do you want me to send ")
                        #message = takeCommand()
                        #kit.sendwhatmsg_to_group()
                        #speak("message has been sent")
                    #except Exception as e:
                        #print(e)
                        #speak("I am not able to send this message")
                else:
                    speak("i am not able to understand")
            else:
                speak("you will not be able to send message! sorry")
            
        elif 'google' in query:
            speak('opening google...')
            query= query.replace("google", "")
            kit.search("" + query)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "who i am" in query:
            speak("If you talk then definately you are a human.")
 
        elif "why you came to world" in query:
            speak("Thanks to John. further It's a secret")
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.get(chrome_path).open("https://www.google.co.in/maps/place/" + location )
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by John")
 
        elif "nucleus" in query:
            wishMe()
            speak("Ready for your service ")
            speak(uname)
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister john")  

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))
       
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what is your name" in query or "What 's your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
    
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'ok' in query:
            speak('Do you need any help sir')

        elif 'no help' in query:
            speak('Do you want me to exit or quit')
            if 'ya' in query:
                exit()
            
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call(["shutdown", "/l"])
         
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
            
        elif "exit" in query or "quit" in query:
            speak('Have a nice day! sir')
            exit()
