from tkinter import *
from register import *
import PyMySQL

class MyStudent:
    def __init__(self):
        root1=Tk()
        root1.title("STUDENT")
        root1.geometry("880x500")
        l=Label(root1,text="STUDENT DETAILS" )
        l.place(x=400 , y=50)
        username=Label(root1,text="USERNAME")
        entry1=Entry(root1)
        password=Label(root1,text="PASSWORD")
        entry2=Entry(root1)
        username.place(x=200,y=100)
        entry1.place(x=400,y=100)
        password.place(x=200 , y=200)
        entry2.place(x=400,y=200)
        b1 = Button(root1, text="LOGIN", font="cyan")
        b1.place(x=350, y=300)
        b2=Button(root1,text="New User?? Register Here",font="cyan",command=MyRegister)
        b2.place(x=300,y=350)
        root1.mainloop()
