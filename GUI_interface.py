from tkinter import *

root = Tk()
root.iconbitmap("Images/microphone.ico")

def click():
    myLabel2 = Label(root, text="Listening...")
    myLabel2.pack()



# # Creating a label widget
# myLabel = Label(root, text="Hi!!!")
myButton = Button(root, text="Listen", padx=50, pady=10, command=click)
# inputField = Entry(root, width=50)
# # Shoving it into the screen
# myLabel.pack()
myButton.pack()
# inputField.pack()
#
root.mainloop()
