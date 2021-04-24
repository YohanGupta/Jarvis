import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)


def speak(audio):  
    engine.say(audio) 
    engine.runAndWait()

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12: 
        speak("Good Morning") 
    elif hour>=12 and hour<=18: 
        speak("Good Afternoon")
    else: 
        speak("Good Evening")
    speak("Hello Yohan!! How may i help you?")

class MainThread(QThread): 
    def __init__(self): 
        super(MainThread,self).__init__()

    def run(self):
        self.taskExecution()

    def takeCommand(self): 
        #It takes microphone command from user and return output
        r = sr.Recognizer()
        with sr.Microphone() as source: 
            print("\nListening...") 
            #my_label2.config(text='Listening...')
            r.pause_threshold = 1  
            r.energy_threshold = 30
            audio = r.listen(source, timeout=10, phrase_time_limit=22)

        try: 
            print('Recognizing')
            #my_label3.config(text="Recognizing...") 
            self.query = r.recognize_google(audio, language="en-IN") 
            print(f"User said: {self.query}\n")
                #my_label4.config(text=f"User said: {query}\n") 
        
        except Exception as e: 
            print("Say that again please...")
            #my_label5.config(text="Say that again please...")
            return "None"
        return self.query
   
    def taskExecution(self):                   
        wishMe()
        while True: 
            self.query = self.takeCommand()
            self.query = self.query.lower()

            #Logic for executing the query
            if 'wikipedia' in self.query:  
                speak("Searching Wikipedia")
                result = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia: ") 
                print(result)
                speak(result) 
                
            elif 'open youtube' in self.query: 
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in self.query: 
                webbrowser.open("https://www.google.com")

            elif 'open icai website' in self.query: 
                webbrowser.open("https://www.icai.org")

            elif 'open github' in self.query: 
                webbrowser.open("github.com")

            elif 'play on my way music' in self.query: 
                webbrowser.open("https://www.youtube.com/watch?v=llGQMlkgkpk") 

            elif 'play any music' in self.query: 
                music_dir = "C:\\Users\\Ritesh\\Music" 
                songs = os.listdir(music_dir) 
                os.startfile(os.path.join(music_dir,songs[0]))

            elif 'the time' in self.query: 
                strTime = datetime.datetime.now().strftime("%H:%H:%S") 
                speak(strTime) 

            elif 'open vs code' in self.query: 
                path = "C:\\Users\\Ritesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
                os.startfile(path)      


startExecution = MainThread()

class Main(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Images/ironman.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Images/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
    

