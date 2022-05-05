from ast import Lambda
import math
from tkinter import *
from tokenize import Number
app ID = ca-app-pub-7412728104073082/6764633603
angel = Tk()
angel.title("Simple Calculator")

e = Entry(angel, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,)

def button_cilck(number):
    # e.delete(0,END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) 

def button_clear():
     e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addtion":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))  

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)




# Define Buttons
btn1 = Button(angel, text="1", padx=40,  pady=20, command=lambda: button_cilck(1))
btn2 = Button(angel, text="2", padx=40,  pady=20, command=lambda: button_cilck(2))
btn3 = Button(angel, text="3", padx=40,  pady=20, command=lambda: button_cilck(3))
btn4 = Button(angel, text="4", padx=40,  pady=20, command=lambda: button_cilck(4))
btn5 = Button(angel, text="5", padx=40,  pady=20, command=lambda: button_cilck(5))
btn6 = Button(angel, text="6", padx=40,  pady=20, command=lambda: button_cilck(6))
btn7 = Button(angel, text="7", padx=40,  pady=20, command=lambda: button_cilck(7))
btn8 = Button(angel, text="8", padx=40,  pady=20, command=lambda: button_cilck(8))
btn9 = Button(angel, text="9", padx=40,  pady=20, command=lambda: button_cilck(9))
btn0 = Button(angel, text="0", padx=40,  pady=20, command=lambda: button_cilck(0))
button = Button(angel, text="+",  padx=39, pady=20, command=button_add)
button_equal = Button(angel, text="=",  padx=91, pady=20, command=button_equal)
button_clear = Button(angel, text="clear",  padx=79, pady=20, command=button_clear)

button_sub = Button(angel, text="-",  padx=41, pady=20, command=button_subtract)
button_mut = Button(angel, text="*",  padx=40, pady=20, command=button_multiply)
button_div = Button(angel, text="/",  padx=41, pady=20, command=button_divide)

# put the buttons on the screen
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)
button.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mut.grid(row=6, column=1)
button_div.grid(row=6, column=2)


angel.mainloop()