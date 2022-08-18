import GUI_interface
import Recognizer
from observed import observable_function
from threading import Thread


def default_setter(arg):
    pass


responseSetter = default_setter

@observable_function
def listen(setter):
    global responseSetter
    responseSetter = setter
    Recognizer.recognize()


def set_response(response):
    responseSetter(response)


def run_gui():
    GUI_interface.run()


if __name__ == "__main__":
    run_gui()
