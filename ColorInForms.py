from hashlib import new
from tkinter import *
from tkinter import messagebox
import random
from tkinter import ttk
# first form
ws = Tk()
ws.title("Color in Forms")
ws.geometry("600x500")
ws.config(bg="#5F9EA0")
ws.attributes('-fullscreen',True)
# second form
def open_ws():
   new= Toplevel(ws)
   new.geometry("600x500")
   new.title("color in forms")
   new.config(bg="#5F9EA0")
   new.attributes('-fullscreen',True)
   Label(new, text ="You are ready to submit your painting estimante!", font=('Sans')).pack(pady=30)
   Button(new, text="Submit").pack(pady=20)
   
frame = Frame(ws, padx=20, pady=20)
frame.pack(expand=True)
Label( ws,text="Hit this next button when you are ready to create your painting estimante!", font=('Sans')).pack(pady=30)
ttk.Button(ws, text="Next", command=open_ws).pack()

# function
def clr():
    fname.delete(0, END)
    lname.delete(0, END)
    em.delete(0, END)
    pn.delete(0, END)
# frames
frame = Frame(ws, padx=20, pady=20)
frame.pack(expand=True)

# labels
Label(
    frame, 
    text="Paint",
    font=("Sans", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)

Label(
    frame, 
    text='Interior or Exterior', 
    font=("Sans", "14")
    ).grid(row=1, column=0, pady=5)

Label(
    frame, 
    text='Color', 
    font=("Sans", "14")
    ).grid(row=2, column=0, pady=5)

Label(
    frame, 
    text='Brand', 
    font=("Sans", "14")
    ).grid(row=3, column=0, pady=5)

Label(
    frame, 
    text='Price Range', 
    font=("Sans", "14")
    ).grid(row=4, column=0, pady=5)
# Entry
fname = Entry(frame, width=30)
lname = Entry(frame, width=30)
em = Entry(frame, width=30)
pn = Entry(frame, width=30)


fname.grid(row=1, column=1)
lname.grid(row=2, column=1)
em.grid(row=3, column=1)
pn.grid(row=4, column=1)

# buttons
clr = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Sans", "14", "bold"), command=clr)
ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Sans", "14", "bold"), command=lambda:ws.destroy())


clr.grid(row=6, column=0, pady=20)
ext.grid(row=6, column=2, pady=20)
def clr():
    fname.delete(0, END)
    lname.delete(0, END)
    em.delete(0, END)
    pn.delete(0, END)
# frames
frame = Frame(ws, padx=20, pady=20)
frame.pack(expand=True)

# labels
Label(
    frame, 
    text="Estimante",
    font=("Sans", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)

Label(
    frame, 
    text='First Name', 
    font=("Sans", "14")
    ).grid(row=1, column=0, pady=5)

Label(
    frame, 
    text='Last Name', 
    font=("Sans", "14")
    ).grid(row=2, column=0, pady=5)

Label(
    frame, 
    text='Email Address', 
    font=("Sans", "14")
    ).grid(row=3, column=0, pady=5)

Label(
    frame, 
    text='Phone Number', 
    font=("Sans", "14")
    ).grid(row=4, column=0, pady=5)
# Entry
fname = Entry(frame, width=30)
lname = Entry(frame, width=30)
em = Entry(frame, width=30)
pn = Entry(frame, width=30)


fname.grid(row=1, column=1)
lname.grid(row=2, column=1)
em.grid(row=3, column=1)
pn.grid(row=4, column=1)

# buttons
clr = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Sans", "14", "bold"), command=clr)
ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Sans", "14", "bold"), command=lambda:ws.destroy())
clr.grid(row=6, column=0, pady=20)
ws.mainloop()