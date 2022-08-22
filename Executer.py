import subprocess
import os
import datetime
import calendar

import Configurations as config


# Returns a string with the current time
def get_time():
    now = datetime.datetime.now()
    if now.minute == 0:
        return f"It's {now.hour} o'clock."
    return f"The time is {now.hour} and {now.minute} minutes."


# Returns a string with the current date
def get_date():
    now = datetime.datetime.now()
    return f"Today is {calendar.month_name[now.month]} {now.day}."


# Search for .exe and run it
def run_exe(program, path):
    program += ".exe"
    for root, dir, files in os.walk(path):
        if program in files:
            subprocess.call([os.path.join(root, program)])
            return True
    return False


# Runs Windows Apps if exists
def run_app(s):
    source = os.popen("powershell -ExecutionPolicy Bypass -Command get-StartApps " + s).read().split()
    if source is not None:
        test = list(filter(lambda e: len(e) > 12, source))
        if test is None or len(test) == 1:
            os.system('start explorer shell:appsfolder\\' + source[-1])
            return True
    return False


# Run the program specified in the command
def open_program(command):
    if "open" in command:
        command.remove("open")
    else:
        command.remove("run")

    # For Microsoft Apps
    if run_app(' '.join(command)):
        return True

    for word in command:
        # For Microsoft Apps
        if run_app(word):
            return True

        # For regular .exe on disk
        if run_exe(word, r"C:\Program Files"):
            return True
        if run_exe(word, r"C:\\"):
            return True
    return False


# Check if client said hi and response
def check_for_hi(command):
    if any(word in command for word in ["hi", "hello"]):
        return "Hello!"
    if all(word in command for word in ["what's", "up"]):
        return "Can't get any better!"
    if all(word in command for word in ["what", "is", "up"]):
        return "I'm fine."
    if all(word in command for word in ["what", "is", "app"]):
        return "I'm OK."
    if all(word in command for word in ["how", "are", "you"]):
        return "I'm fine. Thanks!"


# Check if client said bye, thanks or used bad language and response
def check_for_bye(command):
    # Bye
    if any(word in command for word in ["bye", "goodbye"]):
        return "Good bye."
    if all(word in command for word in ["good", "bye"]):
        return "See you later."
    if all(word in command for word in ["talk", "later"]):
        return "Talk to you later."
    if "stop" in command:
        return "OK, I stopped."

    # Thanks
    if "thanks" in command:
        return "No problem."
    if all(word in command for word in ["thank", "you"]):
        return "You're welcome."

    # Bad language
    if all(word in command for word in ["screw", "you"]):
        return "That is not nice."
    if any(word in command for word in ["f***", "s***", "f******", "ass"]):
        if "you" in command or "your" in command:
            return "That is not nice."
        return "That is some bad language!"


# Execute the command
def execute(command):
    # Check for bye, thanks or bad language
    cfb = check_for_bye(command)
    if cfb is not None:
        return True, cfb

    # Check for greetings
    cfh = check_for_hi(command)
    if cfh is not None:
        return False, cfh

    # For running a program
    if any(word in command for word in ["open", "run"]):
        if open_program(command):
            return True, "OK, Here is " + ' '.join(command) + "."
        return False, "Sorry, I can't find that program.\nTry again."

    # For telling the time or date
    if "time" in command and any(word in command for word in ["what", "what's", "tell"]):
        return True, get_time()
    if "date" in command and any(word in command for word in ["what", "what's", "tell"]):
        return True, get_date()

    # For configurations
    if any(word in command for word in ["change", "switch", "swap"]):

        # For voice change
        if "voice" in command:
            if any(word in command for word in ["female", "woman", "women"]):
                if config.get_voice() == 1:
                    return True, "OK, But I am already a female!"
            if any(word in command for word in ["male", "man", "men"]):
                if config.get_voice() == 0:
                    return True, "OK, But I am already a male!"
            config.change_voice()
            return True, "Voice has been changed."

        # For theme change
        if any(word in command for word in ["theme", "mode"]):
            current_theme = config.get_theme_type()
            if "dark" in command or "black" in command:
                if current_theme == "dark":
                    return True, "It's already dark."
            if "light" in command or "white" in command:
                if current_theme == "light":
                    return True, "It's already light."
            new_theme = "light" if current_theme == "dark" else "dark"
            config.set_theme_type(new_theme)
            return True, "Theme has been changed."

    return False, "Sorry, I didn't understand that."
