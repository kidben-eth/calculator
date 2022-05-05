# importing Tkinter module....
from cgitb import text
from importlib.util import LazyLoader
from random import choice
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor

# set root windows into which all widgets go...
root = Tk()
root.geometry("500x300")
root.title('R E G I S T E R')

def getVals():
    print("Entry Accepted")

# Heading
Label(root, text="Ben Registration Form", font="arial 15 bold").grid(row=0, column=3)

# sets up the Labels Field
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment Mood")
choiceofpayment = Label(root, text="choice of payment")


# packs the Labels Field in the window
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)
choiceofpayment.grid(row=6, column=2)

# sets variable for storing data
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentmoodValue = StringVar()
# choiceofpaymentValue = StringVar()
checkValue = IntVar()


# Creating Entry Fields
nameEntry = Entry(root, textvariable =nameValue)
phoneEntry = Entry(root, textvariable =phoneValue)
genderEntry = Entry(root, textvariable =genderValue)
emergencyEntry = Entry(root, textvariable =emergencyValue)
paymentmoodEntry = Entry(root, textvariable =paymentmoodValue)
choiceofpaymentEntry = Entry(root, textvariable =choiceofpaymentValue)

# packs the Entry Fields
nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergencyEntry.grid(row=4, column=3)
paymentmoodEntry.grid(row=5, column=3)
# choiceofpaymentEntry.grid(row=6, column=3)


# Creating CheckBox
checkbtn = Checkbutton(text="Remember Me?", variable=checkValue)
checkbtn.grid(row=7, column=3)


# Submit Button
button=Button(text="Submit", command=getVals)
button.grid(row=8, column=3)
button["bg"]="blue"
button["fg"]="white"




root.mainloop()