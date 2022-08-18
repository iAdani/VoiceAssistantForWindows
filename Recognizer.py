import sys
import speech_recognition as sr
import pyttsx3
import http.client as client

from Configurations import get_voice as conf_get_voice
from Executer import execute
import Controller

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()
engine.setProperty('rate', 185)
v = engine.getProperty('voices')
engine.setProperty("voice", v[conf_get_voice()].id)


# Answer to the client
def answer(t):
    if engine.getProperty("voice") != conf_get_voice():
        engine.setProperty("voice", v[conf_get_voice()].id)
    engine.say(t)
    engine.runAndWait()
    engine.stop()


# Check if connected to the internet
def check_connection():
    connection = client.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return True
    except:
        answer("Please connect to the internet and try again.")
        connection.close()
    return False


# Parse the command
def parse(command):
    words = command.split()
    # for index, word in enumerate(words):
    for index, word in reversed(list(enumerate(words))):
        if word == "please":
            del words[index]
    return words


# Listen to the client, recognize what they said and execute
def recognize():
    running = True
    while running:
        try:
            # use the microphone as source for input.
            with sr.Microphone() as mic:

                # Wait a moment for the recognizer to adjust the energy threshold based on surrounding noise level
                r.adjust_for_ambient_noise(mic, duration=0.1)

                # Listens for the user's input
                audio = r.listen(mic)

                # Using google to recognize audio
                if not check_connection():
                    break
                text = r.recognize_google(audio)
                text = text.lower()
                text = parse(text)

                # Execute the command
                stop, response = execute(text)
                if response is not None:
                    Controller.set_response(response)
                    answer(response)

                running = not stop

        except sr.UnknownValueError:
            pass
