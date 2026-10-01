# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed"), yk why i put them comments, last time i did't the code broke. weird
def msg():
    messagebox. showwarning("Alert", "Stop! Virus Found. Please scan your computer using your default antivirus software.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus using ur default antivirus", command=msg)
text = Label(root, text="this doesn't do anything, just a test for tkinter")
#joke protegent
protegent_text = Label(root, text="Antivirus is not enough, you need protegent, the only antivirus with deeta recovery software, think secure, think protegent: https://www.protegent.com/")
button.place(x=40, y=80)
text.place(x=40, y=120)
protegent_text.place(x=40, y=140)
# Entering main event loop
root.mainloop()
