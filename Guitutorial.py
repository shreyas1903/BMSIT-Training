from tkinter import *
from turtle import color

SupWdwVav = Tk()

SupWdwVav.title("hello Txt")
SupWdwVav.geometry('500x500')
SupWdwVav.configure(background='blue')


Label(SupWdwVav, text="hello  Inf ",font="arial 35 bold",bg="yellow", fg="brown").grid(row=0, column=1)
Label(SupWdwVav, text="this is sub title",font="arial 20 bold",bg="black", fg="pink").grid(row=3, column=0)


NamIptTxtBoxVav = Entry(SupWdwVav)
NamIptTxtBoxVav.grid(row=9, column=1)


def NamBtnKlkFnc():
	    print("Hello shashank dalle")
	    # CodTdo

Button(SupWdwVav, text="Submit", width=10, command=NamBtnKlkFnc).grid(row=6, column=1)


SupWdwVav.mainloop()