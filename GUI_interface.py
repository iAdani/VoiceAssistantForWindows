import os
from tkinter import *
import psutil
from threading import Thread
from observed import observable_function

from Recognizer import Recognizer
import Configurations


# Kills the process to avoid alive threads from keep running after exit
def kill_process():
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()


class GuiInterface:

    def __init__(self):
        setters = { 'response': self.set_response, 'input': self.set_input,
                    'state': self.set_state, 'theme': self.update_theme }
        self.recognizer = Recognizer(setters)
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
        self.update_theme()
        self.root.mainloop()

    def root_init(self):
        self.root.iconbitmap("Images/logo.ico")
        self.root.title("Voice Assistant")
        self.root.geometry("430x380")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Creating widgets
        self.widgets['listen_button'] = Label(self.root, image=self.mute_img)
        self.widgets['input_label'] = Label(self.root, text="", font=('Mangal', 10), pady=10)
        self.widgets['response_label'] = Label(self.root, text="Click the microphone to start.", font=('Mangal', 11),
                                               pady=10, padx=10)

        # Displaying on the screen
        self.widgets['listen_button'].pack(padx=50, pady=15)
        self.widgets['listen_button'].bind("<Button-1>", self.start_listening)
        self.widgets['input_label'].pack()
        self.widgets['response_label'].pack()

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

    def update_theme(self):
        t = Configurations.get_theme_type()
        config = Configurations.get_theme_config(t)
        self.root.configure(background=config['bg'])
        self.widgets["listen_button"].configure(bg=config['bg'])
        self.widgets["input_label"].configure(bg=config['bg'], fg=config['ifg'])
        self.widgets["response_label"].configure(bg=config['bg'], fg=config['rfg'])
