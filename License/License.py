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
import DateTime.tests.test_datetime
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

class KeyGen():

	def __init__(self):
		global i
		i = int(1)
		print("")
		self.main(i)

	def main(self, count):
		seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

		for i in range(count):
			print('-'.join(''.join(random.choice(seq) for _ in range(5)) for _ in range(5)))

seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
serialkey=('-'.join(''.join(random.choice(seq) for _ in range(5)) for _ in range(5)))

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)
file = open("License.txt", "w")
file.write(str(serialkey+"-"+IPAddress))
file.close()

if __name__ == '__main__':
	app = KeyGen()
