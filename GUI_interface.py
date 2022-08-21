import os
from tkinter import *
import psutil
from threading import Thread
from observed import observable_function

from Recognizer import Recognizer


# Kills the process to avoid alive threads from keep running after exit
def kill_process():
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()


class GuiInterface:

    def __init__(self):
        self.recognizer = Recognizer(self.set_response, self.set_input, self.set_state)
        self.recognizer.recognize.add_observer(self.stop_listening)
        self.state = 0
        self.running = False
        self.t = Thread()
        self.widgets = {}
        self.root = Tk()

        # Images
        self.mic_img = PhotoImage(file=r'Images\mic.png')
        self.mute_img = PhotoImage(file=r'Images\mute.png')

        self.root_init()
        self.root.mainloop()

    def root_init(self):
        self.root.iconbitmap("Images/logo.ico")
        self.root.title("Voice Assistant")
        self.root.geometry("450x350")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Creating widgets
        self.widgets['listen_button'] = Label(self.root, image=self.mute_img)
        self.widgets['input_label'] = Label(self.root, text="", font=('Mangal', 10), pady=10)
        self.widgets['response_label'] = Label(self.root, text="Click the microphone to start.", font=('Mangal', 11),
                                               pady=10, padx=10)

        self.widgets['frame'] = Frame(self.root)

        # Displaying on the screen
        self.widgets['listen_button'].pack(padx=50, pady=15)
        self.widgets['listen_button'].bind("<Button-1>", self.start_listening)
        self.widgets['input_label'].pack()
        self.widgets['response_label'].pack()
        self.widgets['frame'].pack(ipadx=10, ipady=10, expand=True)

    # Window on close handler
    def on_close(self):
        self.root.destroy()
        if self.t.is_alive():
            kill_process()

    def stop_listening(self, arg):
        self.running = False
        self.widgets['listen_button'].configure(image=self.mute_img)

    def listen(self):
        self.recognizer.recognize()

    def start_listening(self, arg):
        if self.t.is_alive():
            return
        self.running = True
        self.widgets['listen_button'].configure(image=self.mic_img)
        self.set_response("Listening...")
        self.t = Thread(target=self.recognizer.recognize, args=(self.recognizer,))
        self.t.start()

    # Set the system's response to the user
    def set_response(self, text):
        self.widgets['response_label'].configure(text=text)

    # Set the user's input to display
    def set_input(self, text):
        self.widgets['input_label'].configure(text=text)

    # Set the current system state
    @observable_function
    def set_state(self, state):
        self.state = state

    def on_state_change(self):
        match self.state:
            case 1:
                pass
