# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets by Alex')
root.geometry('400x300')

# Add widgets
# Add Label
lbl = Label(text="Hello... welcome to the app.", fg="white", bg="#2A5F07",
height=1, width=300)

# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_1b1 = Label(text="Nickname", bg="#38D378")
name_entry = Entry()
# Function to display a Message
def display():
    # Read input given by user
    name = name_entry.get()
    # Declaring a global variable
    # to make it accessible anywhere in the program
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"\n"
    # Display details in a text box
    # Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1,
bg="#12A012", fg='white')

# Organize all the widgets in the window
lbl.pack()
name_1b1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()
