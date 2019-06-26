#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:38:30 2018

@author: Herdt
"""

from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
#from weather import Weather


x = ["EON", "ADS","BMW", "SAP", "TKA","HEN3"]
allocations = [25,25,25,25,25,25]


def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def assistant(command):
    "if statements for executing commands"
    
    if 'test' in command:
        x = 2
        y = 3
        z = x+y

        rand = 'The Value is ' + str(z)
        talkToMe(rand)
        


        
talkToMe('How can i help you Sir')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())           
    