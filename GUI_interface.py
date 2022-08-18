import sys
import tkinter
from tkinter import *
from time import sleep
from threading import Thread
from observed import observable_function
from PIL import Image

import Controller

running = False
t = Thread()


def run():
    # Init
    root = Tk()
    root.iconbitmap("Images/logo.ico")
    root.title("Voice Assistant")
    root.geometry("300x350")

    # Images
    mic_img = PhotoImage(file='Images\mic.png')
    mute_img = PhotoImage(file='Images\mute.png')

    # On close handler
    def on_close():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    def stop_listening(arg):
        global running
        running = False
        listen_button.configure(image=mute_img)

    def start_listening():
        global running, t
        if running is True:
            return
        running = True
        listen_button.configure(image=mic_img)
        set_response("Listening...")
        t = Thread(target=Controller.listen, args=(set_response,))
        Controller.listen.add_observer(stop_listening)
        t.start()

    def set_response(text):
        response_label.configure(text=text)

    def change_theme():
        pass

    # Creating a label widget
    response_label = Label(root, text="Click on the microphone to start.", font=('Mangal', 11), pady=10, padx=10)
    listen_button = Label(root, image=mute_img)
    # Shoving it into the screen
    listen_button.pack(padx=50, pady=15)
    listen_button.bind("<Button-1>", lambda e: start_listening())
    response_label.pack()
    frame = tkinter.Frame(root)
    frame.pack(ipadx=10, ipady=10, expand=True)

    root.mainloop()


if __name__ == "__main__":
    run()
