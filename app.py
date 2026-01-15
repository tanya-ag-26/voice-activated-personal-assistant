import os
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin/flac"

import pyttsx3
import speech_recognition as sr
import datetime
import time

# Initialize text-to-speech engine
engine = pyttsx3.init(driverName='nsss')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

def speak(text):
    print("Assistant:", text)  # visible confirmation
    os.system(f'say "{text}"')

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)
            command = recognizer.recognize_google(audio, language="en-IN")
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand. Please say that again.")
            return ""
        except sr.RequestError:
            speak("Sorry, there is a network issue.")
            return ""

# Greeting
speak("Hello, I am your personal assistant. How can I help you?")

while True:
    command = take_command()
    if command == "":
        continue

    if "hello" in command or "hi" in command:
        speak("Hello! Nice to meet you.")
        time.sleep(1)

    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")
        time.sleep(1)

    elif "date" in command:
        today = datetime.date.today().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
        time.sleep(1)

    elif "day" in command or "today" in command:
        day_name = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day_name}")
        time.sleep(1)

    elif "your name" in command:
        speak("I am a simple voice assistant built using Python.")
        time.sleep(1)

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        break

    elif command != "":
        speak("Sorry, I cannot do that yet.")
        time.sleep(1)