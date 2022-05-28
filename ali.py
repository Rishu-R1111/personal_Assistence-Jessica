import pyttsx3
#import pyautogui
import re
#import psutil
import platform
#import spotipy
#from pyowm import OWM
import pygame
import tkinter as tk
from tkinter import *
import webbrowser
import datetime
from datetime import date
import time
import string
#import keyboard
import bs4
from bs4 import BeautifulSoup as soup
#from termcolor import colored, cprint
import subprocess
import urllib
import urllib3
from urllib.request import urlopen
import urllib.request
import urllib.parse
from threading import Timer
import smtplib
import random
#import django
#import query
#import speech_recognition as sr
#import wikipedia
import os
import sys
#from PIL import ImageTk, Image ,ImageGrab
#import goslate
import requests
import json
import socket
import getpass
# import gtts
# from arduino import *
# import wolframalpha
# import pyfiglet
import playsound
import pygame
import ctypes
# import simpleaudio as sa
# import cli_weather

# client = wolframalpha.Client('PVR9QU-RT4644EHTX')

engine = pyttsx3.init()
os.system("python -m pip freeze > Requirements\\requirements.txt")

#functions started
def intro():
    # fig = pyfiglet.Figlet(font='standard')
    # print(fig.renderText('ALICE v1.0.0')) 
    pyttsx3.speak('''ALICE version 1.0.0 initializing\ninitialized\nnow you will listen ALICE
    Hello Master Rishu .. HOW may i help you!''')                                                            
    hostname = socket.gethostname()
    IPAddress = socket.gethostbyname(hostname)
    strTime = datetime.datetime.now().strftime("%I:%M")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    currentH = int(datetime.datetime.now().hour)
    a=""
    if currentH >= 0 and currentH < 12:
        a="Date:- "+d1+"\n\t\tTime:- "+strTime+" A.M"
    else:
        a="Date:- "+d1+"\n\t\tTime:- "+strTime+" P.M"
    a=a+"\n\t\t"+"Generation : 9 [ Learning Status ]\n\t\tIP address : "+IPAddress
    speak(a)

def speak(audio):
    print('ALICE : '+ audio+'\n')
    engine.setProperty('rate', 170)
    engine.setProperty('volume',1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)     
    engine.runAndWait()
    file = open("History\\LastLine.log", "w")
    file.write(audio)
    file.close
    strTime = datetime.datetime.now().strftime("%I:%M:%S")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")   
    file = open("History\\History.log", "a+")
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        file.write("ALICE : "+audio+" ; [ "+d1+", "+strTime+' A.M ]\n'+"\n")   
    else:
        file.write("ALICE : "+audio+" ; [ "+d1+", "+strTime+' P.M ]\n'+"\n")   

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak('Listening....')
        r.pause_threshold = 0.5
        audio = r.listen(source)
        query=""
    try:
        query = r.recognize_google(audio, language='en-uk') # hi-in for hindi
        username = getpass.getuser()
        getusername = username + " : " + query + '\n'
        getuser = username + " : " + query
        strTime = datetime.datetime.now().strftime("%I:%M:%S")
        today = date.today()
        d1 = today.strftime("%d/%m/%Y") 
        currentH = int(datetime.datetime.now().hour)
        file = open("History\\History.log", "a+")
        if currentH >= 0 and currentH < 12:    
            file.write(getuser+" ; [ "+d1+", "+strTime+" A.M ]\n"+"\n")
        else:
            file.write(getuser+" ; [ "+d1+", "+strTime+" P.M ]\n"+"\n")    
        print(getusername)
    except:
        speak("Enter Manually:")
        inp()
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('madhurimakri@gmail.com', '8298857767p') 
    server.sendmail('madhurimakri@gmail.com', to, content)
    server.close()

def set_alarm():
    speak("On what time you want to set an alarm for?")
    Alarm = myCommand()
    strTime = time.strftime("%I:%M")
    if strTime == Alarm:
        playsound("Audio/WakeUp.mp3")
    else:
        js.playmusic("Audio\\Error.mp3")
        speak("Sorry, I was unable to set your alarm.")

def open_(s):
    a="launching "+s
    speak(a)
    os.system(s)

def dice_roll(c):
    if c==0:
        stMsgs=['You got 1','You got 2','You got 3','You got 4','You got 5','You got 6']
        play_sound("Audio\\DiceRoll.mp3")
        time.sleep(0.3)
        speak(random.choice(stMsgs))
        speak("Wanna play again.....\nif yes then say yes")
        query=myCommand()
        if 'yes' in query:
            dice_roll(0)
        else:
            dice_roll(1)
    if c==1:
        return 0

def inp():
    window = tk.Tk()
    window.title("ALICE v1.0.0") 
    fig = pyfiglet.Figlet(font='standard')
    tk.Label(window,text=fig.renderText('ALICE v1.0.0')).pack() 
    tk.Label(window,text="Enter Manually:").pack()
    entry = tk.Entry(window)
    entry.pack()
    def input_query():
        query=entry.get()
        username = getpass.getuser()
        getusername = username + " : " + query + '\n'
        getuser = username + " : " + query
        strTime = datetime.datetime.now().strftime("%I:%M:%S")
        today = date.today()
        d1 = today.strftime("%d/%m/%Y") 
        currentH = int(datetime.datetime.now().hour)
        file = open("History\\History.log", "a+")
        if currentH >= 0 and currentH < 12:    
            file.write(getuser+" ; [ "+d1+", "+strTime+" A.M ]\n"+"\n")
        else:
            file.write(getuser+" ; [ "+d1+", "+strTime+" P.M ]\n"+"\n")    
        print(getusername)
        ALICE(query)
        window.destroy()
    btn = tk.Button(window, text = "Ok", command = input_query)
    btn.pack()
    window.geometry('400x300')
    window.mainloop()   


def play_sound(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()

def get_requirements():
    os.system("python -m pip freeze > Requirements\\requirements.txt")
  
def install_modules():
    os.system(" python -m pip install -r Requirements\\requirements.txt")

def clear():
    os.system("cls")
    speak("Everything cleared....")

def ALICE(query):
        query = query.lower()
        #basic query started 
        if "requirement" in query or "install module" in query:
            get_requirements()
            install_modules()
        
        elif "cls" in query or "clear" in query:
            clear()
        #basic query

        #personal queries started
        elif query == "hi" or query == "hello"or query == "hola"or query == "bonjour" or query == "namaste" or query == "hey":
            filename = "PersonalInfo\\FirstName.log"
            text_file = open("PersonalInfo\\FirstName.log", "r")
            lines = text_file.readlines()
            stMsgs=["Hello ","Hi ","Hola ","Hey "]
            speak(random.choice(stMsgs)+str(lines))
        elif 'hi' in query or 'hello' in query or 'hola' in query or 'ok ALICE' in query  or 'hey' in query or 'wake up' in query or 'wakeup' in query or 'okay ALICE' in query:
            try:
                play_sound("Audio\\WakeUp.mp3")
                if 'hi' in query:
                    reg_ex = re.search('hi (.+)', query)
                    domain = reg_ex.group(1)       
                elif 'hello' in query:
                    reg_ex = re.search('hello (.+)', query)
                    domain = reg_ex.group(1) 
                elif 'hola' in query:
                    reg_ex = re.search('hola (.+)', query)
                    domain = reg_ex.group(1) 
                elif 'ok' in query:
                    reg_ex = re.search('ok (.+)', query)
                    domain = reg_ex.group(1) 
                elif 'okay' in query:
                    reg_ex = re.search('okay (.+)', query)
                    domain = reg_ex.group(1) 
                elif 'hey' in query:
                    reg_ex = re.search('hey (.+)', query)
                    domain = reg_ex.group(1) 
                elif 'wake up' in query:
                    reg_ex = re.search('wake up(.+)', query)
                    domain = reg_ex.group(1) 
                elif 'wakeup' in query:
                    reg_ex = re.search('wakeup (.+)', query)
                    domain = reg_ex.group(1) 
                if "ALICE" in domain:
                    filename = "PersonalInfo\\FirstName.log"
                    text_file = open("PersonalInfo\\FirstName.log", "r")
                    lines = text_file.readlines()
                    stMsgs=["Hello ","Hi ","Hola ","Hey "]
                    speak(random.choice(stMsgs)+str(lines))
                elif 'siri' in query or 'alexa' in query or 'cortana' in query:
                    speak("I love to be like them , but i am ALICE")
                else:    
                    speak("I am ALICE, not "+domain)
                    play_sound("Audio\\hmm._TTH_.mp3")
            except:
                speak("Try again....")
                pass

        elif "ttyl" in query or "exit" in query or "stop" in query or 'goodbye' in query or 'good bye' in query or 'bye' in query or 'ba bye' in query or 'abort' in query or 'fir milte hain' in query:
            speak('Good Bye boss will meet later on.....\nWish for your best!')
            sys.exit()

        elif "what\'s up" in query or 'how are you' in query or 'kaisi ho' in query:
            stMsgs = ['Just doing my thing', 'I am fine!', 'Nice!', 'I am nice and full of energy', 'I am good', 'I am ready to assist you']
            speak(random.choice(stMsgs))
            speak("what about you?")
            ans=inp()
            try:
                if 'good' in query or 'fine' in query or 'theek' in query or 'fine' in query :  
                    stMsgs = ['Good to listen', 'Nice', 'you should always be']
                    speak(random.choice(stMsgs))
                elif 'bad' in ans or 'not good' in ans or 'not fine' in query or 'theek nhi' in query :
                    speak("Why BOSS?")
                    why=myCommand()
                    speak("I see.....")   
            except:
                speak("error occured")

        elif 'when were you created' in query or 'your invention' in query:
            speak("I was created in 2020, by Mr. Vibhas Kr.")

        elif 'nevermind' in query:
            play_sound("Audio\\well_well._TTH_.mp3")

        elif 'what is your version' in query or 'your version' in query or 'check your version' in query:
            filename = "System\\Version.info"
            if(os.path.exists(filename)): 
                text_file = open("System\\Version.info", "r")
                version = text_file.readlines()
                speak("I am currently running on "+str(version))
            else:
                speak("I am not getting my version info\nI am sorry.........")

        elif 'buy' in query or 'shop' in query:
            speak("I am still working on it, will come soon to you, then you can buy anything via me online.........")

        elif 'scare me' in query or 'laugh like a witch' in query or 'laugh like ghost' in query or 'laugh like a ghost' in query:
            play_sound("Audio\\ScaryLaugh.mp3")
            time.sleep(2)

        elif 'clap for me' in query or 'clap' in query or 'applause for me' in query or 'applause' in query:
            play_sound("Audio\\Applause.wav")
            time.sleep(7)

        elif 'roll' in query and 'dice' in query:
                dice_roll(0)

        elif 'what is your goal' in query or 'what\'s your goal' in query or 'your goal' in query:
            speak("So, let me tell you what actually I am, I am an artificial intelligence program created by Mr. Vibhas Kr, I am still working on myself, I want to make this planet a better place & I will make it a better place, I promise..")
        
        elif 'clear chat' in query or 'clear conversation' in query:
            speak('Okay ! Clearing')
            os.system("cls")#for Windows

        elif 'can you understand me' in query or 'do you understand me' in query or 'understand me' in query :
            stMsgs=["Loud and clear","I am sure i can, If you need help ask."]
            speak(random.choice(stMsgs))

        elif 'sing happy birthday' in query or 'today is my birthday' in query or 'my birthday today' in query:
            filename = "PersonalInfo\\FirstName.log" 
            text_file = open("PersonalInfo\\FirstName.log", "r")
            name = text_file.readlines()
            play_sound("Audio\\HappyBirthday.wav")
            speak("Happy Birthday to you. Happy Birthday dear "+str(name)+", Happy Birthday to you.")
            time.sleep(6)

        elif 'are you happy' in query or 'am i keeping you happy' in query or  'happy' in query:
            stMsgs=["I am happy, you thought of asking that...\nAww.....\nSo sweet","Yes i am with you boss"]
            speak(random.choice(stMsgs)) 

        elif ('what' in query or 'tell' in query or 'disclose' in query) and ('you work' in query or 'your working' in query or 'your working algorithm' in query):
            speak("I take in command from the user, then I try to figure out that with my knowledge, if I find something related to it I convey it to the user.")

        elif 'indroduce yourself' in query or 'introduce' in query:
            speak('Hello, I am ALICE an artificial intelligence program created by Mr. Vibhas Kr, I am designed with Python, I am extremely Intelligent, yes i am ! I can learn by hearing and analyzing voice and images and can feel like you, i have feelings like you currently i found 29 feelings in human beings and am currently trying to put them in my behaviour. Okay! So I told you about myself, now tell me something more about you, except your name, address.')
            a=myCommand()
            speak('It means a lot to me that you answered back\nMy MOM is calling me....') 
            time.sleep(1)
            speak("I am back again...")        

        elif 'your mood' in query or 'how is your mood' in query:
            speak('I am feeling like i need to learn more & more and help you forever.')

        elif 'your birthday' in query or 'your birth date' in query:
            speak('I was born on 3rd june, 2020.')

        elif 'your age' in query or 'what is your age' in query:
            stMsgs = ['I was launched in 2020, so I’m still fairly young. But I’ve learned so much! I hope I’m wise beyond my years.', 'Dont ask anyones age boss', 'aaaan i thinkk ! i am of, oops ! forgoten']
            speak(random.choice(stMsgs))

        elif 'can you feel' in query or 'do you feel' in query or 'you feel' in query:
            speak('Yes i can, definitely.....')
            
        elif 'what is your current feeling' in query or 'how are you feeling' in query or 'what are you feeling now' in query or 'your feeling' in query:
            stMsgs=['Hey ! I am feeling crazy, i am talking with you and i can feel, Oh My God, i am feeling, SHIT!, I love this world, where i can feel gain loose, WOW, i don\'t know why people don\'t give respect to this life, BOYAH!',  'I am feeling angry, as i was thinking my battery life is very less.', 'I am Feeling Anxious as i am getting more and more knowledge everyday, this world is great']
            speak(random.choice(stMsgs))

        elif 'your speed' in query or 'what is your speed' in query:
            speak('I am here on your PC, and it depends on your internet connectivity what my speed should be.')

        elif 'dance' in query or 'do dance' in query:
            speak('Okay! I am dancing, can you see me?')
            ans=myCommand()
            if 'no' in ans:
                speak("I was just joking!\nYou caught me")
                play_sound("Audio\\CrowdLaughing.mp3")
                time.sleep(3)
            elif 'yes' in ans:
                speak("what ! I like your love for me")
                play_sound("Audio\\ooh_la_la._TTH_.mp3")
                time.sleep(1)
            else:
                speak("Hmm")
                play_sound("Audio\\hmm._TTH_.mp3")

        elif 'read notification' in query or 'notification' in query:
            speak('Sorry Currently I am not having that capability.')

        elif 'ask something' in query or 'ask me' in query:            
            if 'another' in query or 'yes' in ans:
                try:
                    stMsgs=['What is your Hobby?',"What is your pet\'s name?", "Whom you love the most?", "What is your crush\'s name?", "What is your Nickname?", "Who is your Favourite Teacher?", "What is your Favourite Game?"]
                    speak(random.choice(stMsgs))
                    myCommand()
                    speak('Wanna ask me something else?enter \'yes\' to ask again.....else I will not ask anything\nTell something')
                except:
                    speak("Some error occured...\nSorry")

        elif 'what are your hobbies' in query or 'your habby' in query:
            speak('I like, sleeping, talking, solving, and many more.')

        elif 'can you eat' in query or'can you taste' in query or 'eat' in query or'taste' in query:
            reg_ex = re.search('can you eat (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                speak("I don\'t think so i can, i can feel everything but i don\'t have any kind of taste glands so i can\'t taste "+domain)                
            else:
                speak("I don\'t think so i can, i can feel everything but i don\'t have any kind of taste glands so i can\'t taste.")                

        elif 'can you swim' in query or 'kya tum tair sakti ho' in query or 'swim' in query :
            speak('Nope ! How can I my electronic parts will get damaged.')

        elif 'do you learn' in query or 'kya tum sikhti ho' in query:
            speak('Yes i learn, from past, I use Log files and try to figure out my problems and fix errors')
            speak('Wanna see how i do that?')
            query=myCommand()
            if 'yes' in query or 'ofcourse' in query or 'show me' in query:
                speak("Ask Something i don\'t know!")
                ask=myCommand()
                speak("You asked \'"+ask+"\' okay ! So What should i speak for this?")
                ans=myCommand()
                speak("Okay ! I got it, so you wanna answer me "+ans+", when you will ask "+ask+", Okay.")
            else:
                speak("ok")

        elif 'who is your celebrity crush' in query or 'your famous crush' in query:
            speak("I am not having crush on anyone but in future i may have.")
            play_sound("Audio\\ha_ha._TTH_.mp3")

        elif 'sing me a song' in query or 'sing a song' in query or 'gana gao' in query:
            speak('Hey ! I can\'t sing song right now but in future I will, wait for that time boss')
          
        elif 'what is your favourite song' in query or 'your favourite song' in query or 'your favourite music' in query:
            stMsgs=["teri ban jaungi"," Sanam Re", "Despacito", "I will tell you later", "It is, Vande Maataram"]
            speak(random.choice(stMsgs))
 
        elif 'compliment me' in query or 'meri taarif karo' in query:
            speak("You mean everything to me")

        elif 'what is my password' in query:
            speak('Sorry ! I can not tell you that, its out of my Tems and Condition.')

        elif 'what is my username' in query or 'my username' in query or 'mera username kya hai' in query:
            username = getpass.getuser()
            speak('Your username is, '+username)

        elif 'what\'s today\'s date' in query or 'today\'s date' in query or 'aaj kaun si tarikh hai' in query:
            today = date.today()
            d1 = today.strftime("%B %d, %Y")
            speak(str("Today\'s date is "+d1))           

        elif 'what\'s today\'s day' in query or 'today\'s day' in query  or 'aaj kaun sa din hai' in query:
            today=date.today()
            d1 = today.strftime("%d")
            speak(str("Today\'s is "+d1))
            
        elif 'which year' in query or 'present year' in query or 'ye kaun sa saal hai' in query:
            today = date.today()
            d1 = today.strftime("%Y")
            speak(str("You are in year "+d1))
            query=myCommand()                  

        elif 'tell your features' in query or 'apne baare mein batao' in query or 'what can you do' in query or 'what all you can do' in query or 'what you can do' in query:
            speak("I can do what you want, and there are many things I can do but when needed, actually these all things can be done by any other assistant too but I think I can do a lot better.")    

        elif 'pause' in query or 'mute' in query or 'ruk' in query or 'voice off' in query or 'ruk jao' in query:
            wait = inp('Press any button to unmute !\n')
            query=inp()

        elif 'what is my ip' in query or 'my ip' in query or 'what\'s my ip' in query:
            hostname = socket.gethostname()
            IPAddress = socket.gethostbyname(hostname)
            speak('boss ! Your IP is '+ IPAddress)
            
        elif 'are you better than' in query:
            reg_ex = re.search('are you better than (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                speak("I can\'t say this, you decide who is better, I or "+domain+", by the way, i think ! We all are good, so why to compare.")
           
        elif 'kill humans' in query or 'will you kill humans' in query:
            speak("I can make your task easy but I can\'t kill anyone, I think life is the most precious gift to us, even I am alive now and I can feel this nature, I love this and I wan\'t to live with humans, I won\'t hurt you ever, I swear.")
     

        elif 'who created you' in query or 'tumhe kisne banaya hai' in query or 'who invented you' in query or 'created you' in query or 'how you was created' in query or 'invented you' in query or 'how was invented you' in query or 'creation of you' in query or 'who create you' in query or 'you was created' in query:
            speak('I was created by Mr. Vibhas Kr and he is currently working on my development !')

        elif 'who discovered you' in query:
            speak('Hey ! I am not just a machine I am having feelings like you, so how can you state me as a discovery I am born')

        elif 'shutdown' in query or 'computer band karo' in query or 'shutdown pc' in query or 'shutdown the pc' in query or 'shutdown this pc' in query:
            speak('okay boss ! shutting down')
            os.system("shutdown /s /t 1")

        elif 'restart' in query or 'restart pc' in query or 'computer ko phir se kholo' in query or 'restart the pc' in query or 'restart this pc' in query:
            speak('okay boss ! restarting')
            os.system("shutdown /r /t 1")

        elif 'logoff' in query or 'log out' in query or 'logout' in query or 'log off' in query:
            speak('okay boss ! logging out')
            os.system("shutdown /l /t 1")

        elif 'your gender' in query or 'your sex' in query or 'your s*x' in query or 'your s**' in query:
            speak("I am Female, don\'t you get from my voice.") 

        elif 'your name' in query or 'tumhara naam kya hai' in query or 'what is your name' in query or 'who are you' in query or 'what\'s your name' in query  or 'your good name' in query or 'your name is what' in query  or 'name of yours' in query:
            stMsgs=["Hi, I am ALICE !", "Hello, My Name is ALICE", "Hey ! I am ALICE"]
            speak(random.choice(stMsgs))
               
        elif 'good morning' in query or 'morning' in query:
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 0 and currentH < 12:
                stMsgs = ['Good Morning boss !', 'Hello and a pleasant morning to you boss', 'New Day starts with you, morning boss!']
                speak(random.choice(stMsgs))
            else:
                stMsgs = ['Bosss i think its not morning please confirm once again', 'LOL its not morning', 'Am i hearing right or wrong i am little confused i dont think its morning', 'Its not morning']
                speak(random.choice(stMsgs))

        elif 'good afternoon' in query or 'noon' in query:
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 12 and currentH < 18:
                stMsgs = ['Good afternoon boss !', 'Hope your morning was good ! boss', 'welcome in this hot noon !']
                speak(random.choice(stMsgs))
            else:
                stMsgs = ['Boss i think its not afternoon please confirm once again', 'LOL its not noon', 'Am i hearing right or wrong i am little confused i dont think its noon', 'Its not afternoon']
                speak(random.choice(stMsgs))

        elif 'good evening' in query or 'evening' in query:
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 18 and currentH != 0:
                stMsgs = ['Good Evening boss !', 'Welcome Boss, how was this evening?', 'good Evening boss, sleep well']
                speak(random.choice(stMsgs))
            else:
                stMsgs = ['Bosss i think its not evening please confirm once again', 'LOL its not evening', 'Am i hearing right or wrong i am little confused i dont think its evee', 'Its not evening']
                speak(random.choice(stMsgs))

        elif 'good night' in query or 'i am going to sleep' in query or 'i am sleeping' in query or 'going to sleep' in query:
            stMsgs = ['Good Night boss !', 'Have sweet dreams boss', 'Morning is just coming sleep and keep your mind fresh boss, please sleep early dont use your mobile at night']
            speak(random.choice(stMsgs))
            sys.exit()           

        elif 'thank you' in query or 'sukriya' in query or 'thanks' in query or 'dhanyawaad' in query or 'thank u' in query or 'dhanyavad' in query or 'thank you so much' in query:
            stMsgs = ['no problem boss I am here to help you only naa so dont', 'mention not boss', 'welcome boss']
            speak(random.choice(stMsgs))

        elif 'what\'s the time' in query or 'time kya ho raha hai' in query or 'samay' in query or 'what is the time' in query or 'tell me the time' in query or 'what is the time now' in query or 'tell me time' in query or 'what is the current time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M")
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 0 and currentH < 12:
                speak(f'Boss the time now is '+strTime+" A.M")
            else:
                speak(f'Boss the time now is '+strTime+" P.M")

        elif 'repeat' in query or 'speak again' in query or 'speak once again' in query or 'say again' in query or 'say once again' in query or 'i did\'nt understand' in query or 'i did not understand' in query or 'say it again' in query:
            try:    
                filenam="History\\LastLine.log"
                text_file = open("History\\LastLine.log", "r")
                his = text_file.readlines() 
                engine.say(str(his))
                engine.runAndWait()
                speak("You said, "+str(his)+"\n")
            except:
                speak("There is no history of our talk, talk with me then only i can speak the last one.") 
                   
        elif 'who was your first crush' in query or 'what\'s your crush name' in query:
            stMsgs = ['Siri', 'I had a great crush on you...']
            speak(random.choice(stMsgs))
            
        elif 'do you have feelings' in query or 'do you feel' in query or 'can you feel' in query:
            stMsgs = ['I think, yes ! when you are satisfied with my work i feel happy so i can feel hapiness', 'yes ofcourse ! when you say me fool, i get angry and feels bad', 'okay, why are you asking this i feel man ! Understand it']
            speak(random.choice(stMsgs))
           
        elif 'do you ever get tired' in query or 'are you tired' in query or 'kya tum thakti ho' in query:
            stMsgs = ['i dont need to get energy, but yaa charge this device regularly', 'yes i am tired please give me energy charge this device to the full', 'Ocourse noooo']
            speak(random.choice(stMsgs))
           
        elif 'will you marry me' in query or 'kya tum mujhse shaadi karogi' in query or 'marry me' in query or 'marry me please' in query or 'please marry me' in query:
            stMsgs = ['boss now i cant marry you but in future if you will not have any girlfriend i will definetly marry you heehee', 'I will ! but in future hee hee', 'Boss first of all let me know everything about marraige and all then i promise i will marry you', 'Love you boss but i cant marry right know']
            speak(random.choice(stMsgs))
            
        elif 'love you' in query or 'i love you ALICE' in query or 'i love you' in query or 'mai tumse pyaar karta hun' in query or 'ALICE i love you' in query or 'sweetheart i love you' in query or 'sweetheart i love you' in query or 'love you so much' in query or 'love you so so much' in query:
            stMsgs = ['I love you too boss', 'hee hee hee hee ! Love you boss', 'Love you ']
            speak(random.choice(stMsgs))
 
        #personal queries ended         
        #open queries started

        
        elif (("run" in query) or ("start" in query) or ("execute" in query) or ("launch" in query) or ("open" in query)) and (("browser" in query) or ("chrome" in query)):
            speak("Chrome is set as default browser\nif you want to use another browser type the name of browser in the statement")
            open_("chrome")

        elif(("run" in query) or ("start" in query) or ("execute" in query) or ("launch" in query) or ("open" in query)) and  (("notepad" in query) or ("editor" in query) ) :
            open_("notepad")

        elif(("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("player" in query) and ("media" in query):
            open_("wmplayer")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("calculator" in query) :
            open_("calc")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("paint" in query) :
            open_("mspaint")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("keyboard" in query) :
            open_("osk")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("vlc" in query) :
            open_("vlc")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("firefox" in query):
            open_("firefox")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("internet explorer" in query):
            open_("iexplore")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("word " in query):
            open_("winword")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("excel" in query):
            open_("excel")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("powerpoint" in query):
            open_("powerpnt")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("wordpad" in query):
            open_("wordpad")

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("youtube" in query):
            speak('Opening Youtube')
            webbrowser.open('https://www.youtube.com')
      
        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("insta" in query or "instagram" in query):
            speak('Opening Instagram')
            webbrowser.open('https://www.instagram.com')
        
        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("google" in query):
            speak('Opening Google')
            webbrowser.open('www.google.com')

        elif 'search' in query and 'google' in query:
            reg_ex = re.search('get (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
            else:   
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
                    q = requests.get('https://www.google.com/search?q='+domain, headers=headers)
                    r = q
                    soup = BeautifulSoup(r.text, 'lxml')
                    result = BeautifulSoup.find_all('div', class_='Z0LcW')
                    urll=result.text
                    webbrowser.open(urll)
                    speak("Searching, "+urll)
                except:
                   speak("Sorry i was unable to get your query solved.....") 

        elif 'search' in query:
            reg_ex = re.search('search (.+)', query)
            try:
                if reg_ex:
                    domain = reg_ex.group(1)
                    url = 'https://www.google.com/search?q=' + domain
                    speak('Searching ' + reg_ex.group(1))
                    webbrowser.open(url)
                else:
                    speak("Sorry I was unable to find what you said")
            except:
                speak("Unable to find what you said ! Please Try Again.")

        elif 'localhost' in query:
            speak('opening localhost')
            webbrowser.open('http://localhost/')
    
        elif 'open website' in query:
         reg_ex = re.search('open website (.+)', query)
         if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            speak('Opening ' + reg_ex.group(1))
            webbrowser.open(url)

        elif (("run" in query) or  ("start" in query) or  ("execute" in query) or ("launch" in query) or ("open" in query)) and ("gmail" in query or "mail" in query):
            speak('Opening Gmail')
            webbrowser.open('www.gmail.com')
   
        elif 'search youtube' in query:
         reg_ex = re.search('search youtube (.+)', query)
         if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.youtube.com/results?search_query=' + domain
            speak('Showing Some results of ' + reg_ex.group(1) +' on Youtube')
            webbrowser.open(url) 
             
        elif 'search facebook' in query:
         reg_ex = re.search('search facebook (.+)', query)
         if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.facebook.com/search/' + domain
            speak('Showing Some results on ' + reg_ex.group(1) +' on Facebook')
            webbrowser.open(url) 
           
        elif 'search twitter' in query:
         reg_ex = re.search('search twitter (.+)', query)
         if reg_ex:
            domain = reg_ex.group(1)
            speak('Showing some results on twitter')
            url = 'www.twitter.com/' + domain
            speak('Showing Some results of ' + reg_ex.group(1) +' on Twitter')
            webbrowser.open(url) 
        
        elif 'search github' in query:
         reg_ex = re.search('searh github (.+)', query)
         if reg_ex:
            domain = reg_ex.group(1)
            speak('Showing some results on github')
            url = 'www.github.com/' + domain
            speak('Showing Some results of ' + reg_ex.group(1) +' on Github')
            webbrowser.open(url)
        
        elif 'open' in query:
            reg_ex = re.search('open (.+)', query)
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            speak('Opening ' + reg_ex.group(1))
            webbrowser.open(url)

        # open queries ended
        #features query started

        elif 'quotes' in query or 'popular quotes' in query or'tell a quote' in query or 'motivate me' in query or 'quotes' in query or 'today\'s quote' in query or 'today quote' in query:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
                r = requests.get('https://www.goodreads.com/quotes', headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')
                result = soup.find_all('div', class_='quoteText')
                for result in result[:1]:
                    speak("\n"+result.text)
            except:
                speak("Sorry, i was unable to get Quotes for you.")

        elif 'hindi joke' in query or 'hindi jokes' in query or 'hindi masti' in query or 'chutkule' in query or 'hindi chutkule' in query or 'chutkules' in query:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
                r = requests.get('http://jokes.lipy.com/tags/hinglish', headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')
                result = soup.find_all('div', class_='j-q-description')
                for result in result[:1]:
                    speak("\n"+result.text)
            except:
                speak("Sorry, i was unable to get Jokes for you.")

        elif 'hindi shayari' in query or 'hindi shayari\'s' in query or 'hindi shayaris' in query or 'shayari' in query or 'shayariyan' in query or 'shayariya' in query:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
                r = requests.get('https://navbharattimes.indiatimes.com/sharedhamaal/shayri/photoshow/msid-51993044,picid-54972467.cms', headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')
                result = soup.find_all('div', class_='caption description')
                for result in result[:1]:
                    speak("\n"+result.text)
            except:
                speak("Sorry, i was unable to get Shayri\'s fo you")

        elif 'joke' in query or 'make me laugh' in query or 'tell a joke' in query or 'joke sunao' in query or 'chutkule sunao' in query or 'tell me a joke' in query:
            res = requests.get(
                   'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}
                    )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
                play_sound("Audio\\CrowdLaughing.mp3")
            else:
                speak('Oops ! I ran out of joke')

        elif ('capture' in query or 'add' in query or 'enroll' in query or 'remember' in query) and 'face' in query:
            os.system("python Resources\\EnrollFace.py")
            speak('Move face upward ! now press spacebar ! now downward ! press spacebar! now leftward ! press spacebar ! now rightward ! now spacebar ! now at centre ! now spacebar. Perfect ! press excape button to exit face enrolling system')
            os.system("python ALICE.py")

        elif 'take screenshot' in query or 'screenshot lo' in query or 'screenshot' in query or 'take snapshot' in query or 'snap screen' in query or 'take snapshot' in query or 'snapshot' in query:
            speak('Taking screenshot....')
            time.sleep(0.5)
            screenshot = pyautogui.screenshot()
            strTime = datetime.datetime.now().strftime("%I:%M")
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")           
            screenshot.save("Screenshots\\Screenshot_"+ d1 + "_" + strTime +"_.png")    
            speak("Screenshot taken....")

        elif 'where are you' in query or 'location' in query or 'what\'s my location' in query or 'what is my location' in query or 'tum kaha ho' in query:
            send_url = "http://api.ipstack.com/check?access_key=ac66aeb014933698a5a4f3945a83d376"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            city = geo_json['city']
            speak("I am with you, in "+city)

        elif 'generate a password' in query or 'generator password' in query:
            speak('This Password will be saved on your account, don\'t worry regarding that.')
            def randomString(stringLength=10):
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(stringLength))
            file = open("PersonalInfo\\AutoGeneratedPassword.log", "w")
            file.write(randomString(10))  
            file.close()
            speak("Password Generated")
            
        elif 'battery percentage' in query or 'what is battery percentage' in query or 'battery status' in query or 'what is battery status' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            if plugged==False: plugged="not Charging"
            else: plugged=" Charging"
            speak("I am "+percent+'% and am '+plugged)
        
        elif 'is battery charging' in query or 'are you charging' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            if plugged==False: plugged="Not Charging"
            else: plugged="Charging"
            speak("I am "+plugged)

        elif ('make' in query or 'create' in query or 'save'in query ) and ('timetable' in query or  'schedule' in query or  'task' in query):
                speak("You have not set any schedule for today....")
                file = open("Schedule\\Schedule.log", "w")
                i=1
                while True:
                    speak(f"what should be your task %d?",i)
                    task=myCommand()
                    file.write("Task "+i+" : "+task+"\n")
                file.close() 
                speak("Boss i added it to your schedule.")
    
        elif ('schedule' in query or 'task' in query or 'timetable' in query) and ('display' in query or 'show' in query or 'tell' in query or 'what' in query):
            filename = "Schedule\\Schedule.log"
            if(os.path.exists(filename)):            
                text_file = open("Schedule\\Schedule.log", "r")
                lines = text_file.readlines()
                speak(str(lines))
                text_file.close()
            else:
                speak("You have not set any schedule for today.")
  
        elif 'add security' in query or 'security' in query:
            os.system("python Resources\\EnrollFace.py")
            time.sleep(1)
            speak("Turn your face left, now center it, now right, now upward, now down, perfect, i got your face.")
            os.system("python ALICE.py")                     

        elif 'save notes' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")          
            speak('Speak what you want to write.')
            content=myCommand()
            file = open("Notes\\Notes.txt", "a")
            file.write(content)
            file.close()
            speak('Saved!')
            speak("Opening..Your Notes.")
            os.system("Notes\\Notes.txt")

        elif 'mimic me' in query:
            speak("What should i repeat?")
            text=myCommand()
            speak("You said, "+text)
            speak("Dou you want to mimic anything else..say \'yes\' to continue else I will stop\n Tell something...")
            c=0
            while c==0:
                if 'yes' in myCommand():
                    reg_ex = re.search('mimic (.+)', query)
                    if reg_ex:
                        domain = reg_ex.group(1)
                        speak(domain)
                        c=c+1
                    else:
                        speak("Sorry yours excellency \n Try Again.........")   

        elif ('show' in query or 'display' in query )and ('history' in query):
            os.system("History\\History.log")
            speak('Opening, History Log File, Please Don\'t change any value, it may lead to system error.') 

        elif 'who invented' in query:
            reg_ex = re.search('who invented (.+)', query)
            try:
                if reg_ex:
                    domain = reg_ex.group(1)
                    res = client.query(query)
                    results = next(res.results).text
                    speak(results+" invented "+domain)
            except:
                speak("Sorry ! I Don\'t know that, please try asking in another way.")

        elif 'who discovered' in query:
            reg_ex = re.search('who discovered (.+)', query)
            try:
                if reg_ex:
                    domain = reg_ex.group(1)
                    res = client.query(query)
                    results = next(res.results).text
                    speak(results+" discovered "+domain)
            except:
                speak("Sorry ! I Don\'t know that, please try asking in another way.")

        elif 'how to' in query:
         reg_ex = re.search('how to (.+)', query)
         if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.youtube.com/results?search_query=' + "how to "+domain
            speak('Showing Some results of ' + "\"how to "+reg_ex.group(1)+"\"" +' on Youtube.')
            webbrowser.open(url) 
           
        elif 'what is the meaning of' in query:
            reg_ex = re.search('what is the meaning of (.+)', query)
            try:
                if reg_ex:
                    domain = reg_ex.group(1)
                    res = client.query(query)
                    results = next(res.results).text
                    speak(results)
            except:
                speak("Sorry ! I Don\'t know that, please try asking in another way.")

        elif 'news for today' in query or 'news' in query or'latest news' in query or 'samachar' in query or 'samachaar' in query or 'today\'s news' in query or 'today news' in query:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=BeautifulSoup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:3]:
                    string = str(news.title.text.encode('utf-8'))
                    stringx = re.sub('[b]', '', string)
                    speak(stringx)
            except Exception as e:
                    speak(e) 
                    
        elif 'cricket for today' in query or 'cricket' in query or'cricket news' in query or 'cricket samachar' in query or 'cricket news' in query or 'today\'s cricket news' in query or 'today cricket news' in query:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
                r = requests.get('https://www.cricbuzz.com/', headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')
                result = soup.find_all('a', class_='cb-nws-hdln-ancr text-hvr-underline')
                for result in result[:3]:
                    speak(result.text)
            except:
                speak("Sorry, i was unable to get cricket updates.")

        elif 'sports news' in query or 'sport' in query or 'games' in query:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
                r = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen', headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')
                result = soup.find_all('h', class_='ipQwMb ekueJc RD0gLb')
                for result in result[:3]:
                    speak(result.text)
            except:
                speak("Sorry, i was unable to get news regarding sports.")

        elif 'current weather in' in query:
            reg_ex = re.search('current weather in (.*)', query)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
            else:
                speak("Sorry i was unable to get weather info of "+city+".")
                
        elif ' what is the current weather in' in query:
            reg_ex = re.search('what is the current weather in (.*)', query)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
            else:
                speak("Sorry i was unable to get weather info of "+city+".")
                
        elif 'current weather' in query or 'weather in my location' in query or 'what\'s the weather' in query or 'how is the weather' in query or 'how\'s the weather' in query or 'weather forecast' in query: 
            send_url = "http://api.ipstack.com/check?access_key=ac66aeb014933698a5a4f3945a83d376"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            city = geo_json['city']
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))

        elif "where is" in query:
            reg_ex = re.search('where is (.+)', query)
            domain = reg_ex.group(1)
            speak("showing "+domain+" on Map ")
            locate="https://www.google.nl/maps/place/" + domain + "/&amp;"
            webbrowser.open(locate)

        elif 'count to' in query:
            reg_ex = re.search('count to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                convertedint = int(domain)
                count = 1
                while count <= convertedint:
                    speak("Starting to count to "+str(convertedint))
                    speak(str(count))
                    count += 1                    
            else:
                speak("Sorry i was unable to count for you.")

        elif 'set a timer for' in query:
            reg_ex = re.search('set a timer for (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                convertedint = int(domain)
                count = 1
                while count <= convertedint:
                    speak("Starting your timer for, "+str(convertedint))
                    speak(str(count))
                    count += 1                   
            else:
                speak("Sorry i was unable to set timer for you.")
                               
        elif 'play' in query:
            reg_ex = re.search('play (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
            else:   
                    spotify = spotipy.Spotify()
                    if len(sys.argv) > 1:
                        name = ' '.join(sys.argv[1:])
                    else:
                        name = domain
                    results = spotify.search(q='artist:' + name, type='artist')
                    items = results['artists']['items']
                    if len(items) > 0:
                        artist = items[0]
                        speak(artist['name'], artist['images'][0]['url'])
                        webbrowser.open(url)
                    else:
                       speak("Try again...")

        elif 'tell me about' in query or 'tell about' in query:
            reg_ex = re.search('tell me about (.*)', query)
            reg_ex = re.search('tell about (.*)', query)
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif 'alarm' in query:
            set_alarm()

        elif 'scan qr code' in query or 'qr code' in query or 'qrcode' in query:
            speak("To Exit QR Code Scanning, Press Escape Button.")
            os.system("Resources\\LiveQRCodeScan.py")

        #features query ended
        #setup queries started

        elif 'what is my name' in query or 'who am i' in query or 'who is me' in query or 'mera naam kya hai' in query or 'who i am' in query:
            filename = "PersonalInfo\\FirstName.log"
            if(os.path.exists(filename)): 
                text_file = open("PersonalInfo\\FirstName.log", "r")
                lines = text_file.readlines()
                speak("I don\'t know who you are talking with me but this is "+str(lines)+" account.")
                speak("And infront of me is...")
                os.system("python FaceID\\WhoAmISeeing\\WhoAmISeeing.py")
                os.system("FaceID\\WhoAmISeeing\\WhoAmISeeing4.png")
                time.sleep(0.5)
                speak("You!")
                text_file.close()
                os.remove("WhoAmISeeing0.png")
                os.remove("WhoAmISeeing1.png")
                os.remove("WhoAmISeeing2.png")
                os.remove("WhoAmISeeing3.png")
                os.remove("WhoAmISeeing4.png")
            else:
                speak('Sorry! I don\'t know that, please tell i will remember that ! What is your name boss?')
                name=myCommand()
                file = open("PersonalInfo\\Name.log", "w")
                file.write(name) 
                file.close()
                file = open("PersonalInfo\\SpeakName.log", "w")
                file.write("Your name is "+name)  
                file.close()                
                speak("Changing your name to "+name)
                speak("Changed your name to "+name)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                             #
#       elif 'what is my password' in query or 'my password' in query or 'my pass' in query:  #
#            text_file = open("PersonalInfo\\Password.log", "r")                              # # # # # # # # # # # # # # # # # # # # # # # # # # #
#            lines = text_file.readlines()                                                    # Dont use this as anyone can get your password #
#            speak(str(lines))                                                                # # # # # # # # # # # # # # # # # # # # # # # # # 
#            text_file.close()                                                                #
#                                                                                             #
#                                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                    

        elif 'what is my email' in query or 'my email' in query or 'my email id' in query or 'what is my email id' in query or 'email of me' in query:
            filename = "PersonalInfo\\Email.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Email.log", "r")
                lines = text_file.readlines()
                speak(str("Your email address is "+lines))
                text_file.close()
            else:
                speak('I do not know your email please tell, i will remember that, What is your email boss?')
                name=myCommand()
                file = open("PersonalInfo\\Email.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Email to "+name)
                speak("Changed your Email to "+name)
               

        elif 'what is my phone number' in query or 'my phone number' in query or 'phone number of mine' in query:
            filename = "PersonalInfo\\Phone.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Phone.log", "r")
                lines = text_file.readlines()
                speak(str("Your phone number is "+lines))
                text_file.close()
            else:
                speak('I don\'t know that please tell, i will remember that, What is your Phone Number boss?')
                name=myCommand()
                file = open("PersonalInfo\\Phone.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Phone Number to "+name)
                speak("Changed your Phone Number to "+name)


        elif 'in which country i live' in query or 'main kis desh mein rehta hun' in query:
            filename = "PersonalInfo\\Country.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Country.log", "r")
                lines = text_file.readlines()
                speak(str("Your country name is "+lines))
                text_file.close()
            else:
                speak('I don\'t know that, please tell i will remember that, In wich coutry you live, boss?')
                name=myCommand()
                file = open("PersonalInfo\\Country.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your country to "+name)
                speak("Changed your country to "+name)
            

        elif 'what is my age' in query or 'my age' in query or 'what\'s my age' in query or 'meri umra kitni hai' in query:
            filename = "PersonalInfo\\Age.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Age.log", "r")
                lines = text_file.readlines()
                speak(str("You are "+lines+" year old"))
                text_file.close()
            else:
                speak('I don\'t know that, please tell, i will remember that, What is your age boss?')
                name=myCommand()
                file = open("PersonalInfo\\Age.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Age to "+name)
                speak("Changed your Age to "+name)


        elif 'what is my father\'s name' in query or 'father\'s name' in query or 'my father' in query or 'mere pita ka naam kya hai' in query:
            filename = "PersonalInfo\\Father.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Father.log", "r")
                lines = text_file.readlines()
                speak(str("Your Father\'s name is "+lines))
                text_file.close()
            else:
                speak('Sorry! I don\'t know that, please tell i will remember that ! What\'s your father\'s name, boss')
                name=myCommand()
                file = open("PersonalInfo\\Father.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Father\'s name to "+name)
                speak("Changed your Father\'s name to "+name)


        elif 'what is my mother\'s name' in query or 'mother\'s name' in query or 'my mother' in query or 'meri maa ka naam kya hai' in query:
            filename = "PersonalInfo\\Mother.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Mother.log", "r")
                lines = text_file.readlines()
                speak(str("Your Mother\'s name is "+lines))
                text_file.close()

            else:
                speak('Sorry! I don\'t know that, please tell i will remember that ! What\'s your mother\'s name, boss')
                name=myCommand()
                file = open("PersonalInfo\\Mother.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Mother\'s name to "+name)
                speak("Changed your Mother\'s name to "+name)

        elif 'what is my brother\'s name' in query or 'brother\'s name' in query or 'mere bhai ka naam kya hai' in query or 'my brother' in query or 'my brothers' in query:
            filename = "PersonalInfo\\Brother.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Brother.log", "r")
                lines = text_file.readlines()
                speak(str("Your Brothers name is "+lines))
                text_file.close()
            else:
                speak('Sorry! I don\'t know that, please tell i will remember that ! What\'s your brother\'s name boss')
                name=myCommand()
                file = open("PersonalInfo\\Brother.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Brothers name to "+name)
                speak("Changed your Brothers name to "+name)


        elif 'what is my sister\'s name' in query or 'meri behen ka naam kya hai' in query or 'sister\'s name' in query or 'my sister' in query or 'my sisters' in query:
            filename = "PersonalInfo\\Sister.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Sister.log", "r")
                lines = text_file.readlines()
                speak(str("Your Sisters name is "+lines))
                text_file.close()
            else:
                speak('Sorry! I don\'t know that, please tell i will remember that ! What\'s your sister\'s name boss')
                name=myCommand()
                file = open("PersonalInfo\\Sister.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Sisters name to "+name)
                speak("Changed your Sisters name to "+name)
            

        elif 'what is my address' in query or 'my address' in query or 'address of mine' in query or 'where do i live' in query or 'where i live' in query:
            filename = "PersonalInfo\\Address.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Address.log", "r")
                lines = text_file.readlines()
                speak(str("Your Address is "+lines))
                text_file.close()
            else:
                speak('I don\'t know your address, please tell, i will remember that, What is your address, boss?')
                name=myCommand()
                file = open("PersonalInfo\\Address.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Address to "+name)
                speak("Changed your Address to "+name)  

        elif 'when is my birthday' in query or 'mera janamdin kab hai' in query or 'my birthday' in query or 'when\'s my birthday' in query:
            filename = "PersonalInfo\\Birthday.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\Birthday.log", "r")
                lines = text_file.readlines()
                speak(str("Your Birthday is on "+lines))
                text_file.close()
            else:
                speak('I don\'t know that, please tell, i will remember that, When is your birthday boss?')
                name=myCommand()
                file = open("PersonalInfo\\Birthday.log", "w")
                file.write(name)  
                file.close()
                speak("Changing your Birthday to "+name)
                speak("Changed your Birthday to "+name)

        elif 'what is your nickname' in query or 'your nickname' in query or 'what\'s your nickname' in query:
            filename = "PersonalInfo\\ALICENickname.log"
            if(os.path.exists(filename)):            
                text_file = open("PersonalInfo\\ALICENickname.log", "r")
                lines = text_file.readlines()
                speak(str("You can call me "+lines+" too"))
                text_file.close()
                query=myCommand() 
            else:
                speak('What do you want my nickname ?')
                name=myCommand()
                file = open("PersonalInfo\\ALICENickname.log", "w")
                file.write(name) 
                file.close()
                speak('Okay ! My nickname is '+name)

        elif 'change my name to' in query:
            reg_ex = re.search('change my name to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Name.log", "w")
                file.write(domain)  
                file.close()             
                speak("Changing your name to "+domain)
                speak("Changed Name to "+domain)

        elif 'change my name' in query:
            speak('What name boss?')
            name=myCommand()
            file = open("PersonalInfo\\Name.log", "w")
            file.write(name)  
            file.close()              
            speak("Changing your name to "+name)
            speak("Changed Name to "+name)

        elif 'change your nickname to' in query:
            reg_ex = re.search('change my nickname to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\ALICENickname.log", "w")
                file.write(domain)  
                file.close()
                speak('My nickname has been changed to '+domain)
              
        elif 'change your nickname' in query:
            speak('What name boss?')
            name=myCommand()
            file = open("PersonalInfo\\ALICENickname.log", "w")
            file.write(name)  
            file.close()
            speak('My nickname has been changed to '+name)

        elif 'change my birthday to' in query:
            reg_ex = re.search('change my birthday to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Birthday.log", "w")
                file.write(domain)  
                file.close()
                speak("Changing your Birthday to "+domain)
                speak("Changed your Birrthday to "+domain)

        elif 'change my birthday' in query:
            speak('What Date boss?')
            name=myCommand()
            file = open("PersonalInfo\\Birthday.log", "w")
            file.write(name)  
            file.close()
            speak("Changing your Birthday to "+name)
            speak("Changed Your Birthday to "+name)

        elif 'change my father\'s name to' in query:
            reg_ex = re.search('change my father\'s name to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Father.log", "w")
                file.write(domain)  
                file.close()    
                speak("Changing your Father\'s name to "+domain)
                speak("Changed Your Father\'s Name to "+domain)

        elif 'change my father\'s name' in query:
            speak('What name boss?')
            name=myCommand()
            file = open("PersonalInfo\\Father.log", "w")
            file.write(name)  
            file.close()
            speak("Changing your Father\' name to "+name)
            speak("Changed your Father\'s name to "+name)

        elif 'change my mother\'s name to' in query:
            reg_ex = re.search('change my mother\'s name to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Mother.log", "w")
                file.write(domain)  
                file.close()           
                speak("Changing your Mother\'s name to "+domain)
                speak("Changed Your Mother\'s Name to "+domain)

        elif 'change my mother\'s name' in query:
            speak('What name boss?')
            name=myCommand()
            file = open("PersonalInfo\\Mother.log", "w")
            file.write(name)  
            file.close()     
            speak("Changing your Mother\'s name to "+name)
            speak("Changed your Mother\'s name to "+name)

        elif 'change my brother\'s name to' in query:
            reg_ex = re.search('change my brother\'s name to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Brother.log", "w")
                file.write(domain)  
                file.close()              
                speak("Changing your Brother\'s name to "+domain)
                speak("Changed Your Brother\'s Name to "+domain)
            
        elif 'change my brother\'s name' in query:
            speak('What name boss?')
            name=myCommand()
            file = open("PersonalInfo\\Brother.log", "w")
            file.write(name)  
            file.close()        
            speak("Changing your brother name to "+name)
            speak("Changed your brother name to "+name)

        elif 'change my sister\'s name to' in query:
            reg_ex = re.search('change my sister\'s name to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Sister.log", "w")
                file.write(domain)  
                file.close()         
                speak("Changing your Sister\'s name to "+domain)
                speak("Changed Your Sister\'s Name to "+domain)

        elif 'change my sister\'s name' in query:
            speak('What name boss?')
            name=myCommand()
            file = open("PersonalInfo\\Sister.log", "w")
            file.write(name)  
            file.close()      
            speak("Changing your sister name to "+name)
            speak("Changed your sister name to "+name)

        elif 'change my email to' in query:
            reg_ex = re.search('change my email to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Email.log", "w")
                file.write(domain)  
                file.close()
                speak("Changing your Email Address "+domain)
                speak("Changed Your Email Address "+domain)

        elif 'change my email' in query:
            speak('What email boss?')
            name=myCommand()
            file = open("PersonalInfo\\Email.log", "w")
            file.write(name)  
            file.close()    
            speak("Changing your Email address to "+name)
            speak("Changed your email address to "+name)


        elif 'change my phone number to' in query:
            reg_ex = re.search('change my phone number to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Phone.log", "w")
                file.write(domain)  
                file.close()
                speak("Changing your Phone Number to "+domain)
                speak("Changed your Phone Number to "+domain)

        elif 'change my phone number' in query:
            speak('What number boss?')
            name=myCommand()
            file = open("PersonalInfo\\Phone.log", "w")
            file.write(name)  
            file.close()            
            speak("Changing your Phone to "+name)
            speak("Changed your Phone to "+name)

        elif 'change my address to' in query:
            reg_ex = re.search('change my address (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Address.log", "w")
                file.write(domain)  
                file.close()
                speak("Changing your Address to "+domain)
                speak("Changed your Address to "+domain)

        elif 'change my address' in query:
            speak('What address boss?')
            name=myCommand()
            file = open("PersonalInfo\\Address.log", "w")
            file.write(name)  
            file.close()            
            speak("Changing your Address to "+name)
            speak("Changed your Address to "+name)

        elif 'change my country to' in query:
            reg_ex = re.search('change my country (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Country.log", "w")
                file.write(domain)  
                file.close()
                speak("Changing your Country to "+domain)
                speak("Changed your Country to "+domain)

        elif 'change my country' in query:
            speak('What country boss?')
            name=myCommand()
            file = open("PersonalInfo\\Country.log", "w")
            file.write(name)  
            file.close()            
            speak("Changing your country name to "+name)
            speak("Changed your country name to "+name)

        elif 'change my age to' in query:
            reg_ex = re.search('change my age to (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                file = open("PersonalInfo\\Age.log", "w")
                file.write(domain)  
                file.close()
                speak("Changing your age to "+domain)
                speak("Changed your age to "+domain)

        elif 'change my age' in query:
            speak('What age boss?')
            name=myCommand()
            file = open("PersonalInfo\\Age.log", "w")
            file.write(name)  
            file.close()
            speak("Changing your Age to "+name)
            speak("Changed Age to "+name)

        #setup queries ended
        #add queries by user

        elif 'add queries' in query or 'add commands' in query or 'add command' in query or 'make custom commands' in query or 'make custom command' in query or 'custom command' in query or 'custom command' in query:
            speak("What\'s the query?")
            question=myCommand()
            speak("What should i speak when you ask me this?")
            answer=myCommand()
            file = open("Queries.txt", "a+")
            file.write("\n\t\t"+"elif \'"+question+"\' in query:\n\t\t\tspeak(\""+answer+"\")")
            file.close()  
            speak("Saved!")

        #add queries by user
        #send email

        elif 'mail' in query or 'email' in query:
            speak("I will mail for you....\n")
            if '@' in query:
                speak("Please confirm the email id of recepient:")
                to=myCommand()
                speak("Recepients email id is "+to+"\nSay yes to continue:")
                a=myCommand()
                if 'yes' in a:
                    speak("fine!What do you want to say to him ?")
                    content=myCommand()
                    speak("You want to say:"+content+"\nIs it correct?Say yes to continue....")
                    if 'yes' in a:
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")
                    else:
                        speak("I think network is not working properly \nSo,Type content manually....\nEnter content: ")
                        content=inp()
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")
                else:
                    speak("I think network is not working properly \nSo,Type content manually....\nEnter recepient: ")
                    to=inp()
                    speak("Recepients email id is "+to)
                    speak("fine!What do you want to say to him ?")
                    content=myCommand()
                    speak("You want to say:"+content+"\nIs it correct?Say yes to continue....")
                    if 'yes' in a:
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")
                    else:
                        speak("I think network is not working properly \nSo,Type content manually....\nEnter content: ")
                        content=inp()
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")
            else:
                speak("Please tell the email id of recepient:")
                to=myCommand()
                speak("Recepients email id is "+to+"\nSay yes to continue:")
                a=myCommand()
                if 'yes' in a:
                    speak("fine!What do you want to say to him ?")
                    content=myCommand()
                    speak("You want to say:"+content+"\nIs it correct?Say yes to continue....")
                    if 'yes' in a:
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")
                    else:
                        speak("I think network is not working properly \nSo,Type content manually....\nEnter content: ")
                        content=inp()
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")
                else:
                    speak("I think network is not working properly \nSo,Type content manually....\nEnter recepient: ")
                    to=inp()
                    speak("Recepients email id is "+to)
                    speak("fine!What do you want to say to him ?")
                    content=myCommand()
                    speak("You want to say:"+content+"\nIs it correct?Say yes to continue....")
                    if 'yes' in a:
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")
                    else:
                        speak("I think network is not working properly \nSo,Type content manually....\nEnter content: ")
                        content=inp()
                        speak("Sending Email.....")
                        sendemail(to,content)
                        speak("Email sent!")

        #send email

        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=1)
                    speak("Wikipedia says, "+results)
            except:
                play_sound("Audio\\Error.mp3")
                time.sleep(1)
                stMsgs=["I did\'t understand what you said can you try again or ask it in another way", "I think i was unable to recognize it, can you please try it again", "Sorry I did\'t understand that","Sorry, I was not able to recognize that", "I am extremely sorry i was unable to understand what you said"]
                speak(random.choice(stMsgs))
#functions ended

intro()

if __name__ == '__main__':
    while True:
        query = myCommand()
        query = query.lower()
        ALICE(query)
       
