# # Python program to translate
# # speech to text and text to speech
#
#
# import speech_recognition as sr
# import pyttsx3
#
# # Initialize the recognizer
# r = sr.Recognizer()
#
#
# # Function to convert text to
# # speech
# def SpeakText(command):
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()
#
#
# # Loop infinitely for user to
# # speak
#
# while (1):
#
#     # Exception handling to handle
#     # exceptions at the runtime
#     try:
#
#         # use the microphone as source for input.
#         with sr.Microphone() as source2:
#
#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.2)
#
#             # listens for the user's input
#             audio2 = r.listen(source2)
#
#             # Using google to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()
#
#             print("Did you say " + MyText)
#             SpeakText(MyText)
#
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#
#     except sr.UnknownValueError:
#         print("unknown error occured")


# Returns a list with Windows Apps on this pc and the run source
# def get_apps_list():
#     apps = os.popen("powershell -ExecutionPolicy Bypass -Command get-StartApps").read().split()
#     apps = list(filter(None, apps))
#     lst = []
#     e = ''
#     for app in apps:
#         if len(app) < 15:
#             e = e + app + ' '
#         else:
#             lst.append(e[:-1])
#             e = ''
#     return lst

import os
import re
import subprocess

import Configurations
from Recognizer import recognize
import yaml

#
# def run_exe(program, path):
#     program += ".exe"
#     for root, dir, files in os.walk(path):
#         if program in files:
#             subprocess.call([os.path.join(root, program)])
#             return True
#     return False

from observed import observable_function
import time


# @observable_function
# def hi():
#     print("hi")
#     time.sleep(2)
#     print("bye")
#
#
# def observer():
#     print("SUP")

from tkinter import Tk, font

if __name__ == '__main__':
    # recognize()
    root = Tk()
    print(font.families())
    # apps = os.popen("powershell -ExecutionPolicy Bypass -Command get-StartApps").read().split()
    # apps = list(filter(None, apps))
    # lst = []
    # e = ''
    # for app in apps:
    #     if len(app) < 15:

    #     else:
    #         lst.append(e[:-1])
    #         e = ''
    # apps = lst
    # for string in apps:
    #     print(string)
    # with open('config.yaml') as f:
    #     data = yaml.load(f, Loader=yaml.FullLoader)
    #     print(data)
    # print (Configurations.config)
    # Configurations.change_voice(0)
    # print (Configurations.config)


