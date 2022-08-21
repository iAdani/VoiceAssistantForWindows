import speech_recognition as sr
import pyttsx3
import http.client as client
from observed import observable_function

from Configurations import get_voice as conf_get_voice
from Executer import execute

NO_CONNECTION_RESPONSE = "Please connect to the internet and try again."


# Check if connected to the internet
def check_connection():
    connection = client.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return True
    except:
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


class Recognizer:

    def __init__(self, response_setter, input_setter, state_setter):
        # Set the setters
        self.response_setter = response_setter
        self.input_setter = input_setter
        self.state_setter = state_setter

        # Initialize the recognizer
        self.r = sr.Recognizer()

        # Initialize the engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 185)
        v = self.engine.getProperty('voices')
        self.engine.setProperty("voice", v[conf_get_voice()].id)

    # Answer to the client
    def answer(self, t):
        if self.engine.getProperty("voice") != conf_get_voice():
            v = self.engine.getProperty('voices')
            self.engine.setProperty("voice", v[conf_get_voice()].id)
        self.engine.say(t)
        self.engine.runAndWait()
        self.engine.stop()

    # Listen to the client, recognize what they said and execute
    @observable_function
    def recognize(self):
        running = True
        i = 0
        while running and i < 2:
            try:
                # use the microphone as source for input.
                with sr.Microphone() as mic:

                    # Wait a moment for the recognizer to adjust the energy threshold based on surrounding noise level
                    self.r.adjust_for_ambient_noise(mic, duration=0.1)

                    # Listens for the user's input
                    audio = self.r.listen(mic)

                    # Using google to recognize audio
                    if not check_connection():
                        self.response_setter(NO_CONNECTION_RESPONSE)
                        self.answer(NO_CONNECTION_RESPONSE)
                        break
                    text = self.r.recognize_google(audio)
                    self.input_setter(text)
                    text = text.lower()
                    text = parse(text)

                    # Execute the command
                    stop, response = execute(text)
                    if response is not None:
                        self.response_setter(response)
                        self.answer(response)

                    running = not stop
                    i = i + 1

            except sr.UnknownValueError:
                pass

    # response = "Sorry, I didn't hear you."
    # Controller.set_response(response)
    # answer(response)
