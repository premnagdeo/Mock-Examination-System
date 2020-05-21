from tkinter import *
from question import *
import PyMySQL
class MyAdmin:
    def __init__(self):
        root2= Tk()
        root2.title("ADMIN")
        root2.geometry("880x500")
        l=Label(root2,text="Admin Login" )
        l.place(x=400 , y=50)
        username=Label(root2,text="USERNAME")
        entry1=Entry(root2)
        password=Label(root2,text="PASSWORD")
        entry2=Entry(root2)
        username.place(x=200,y=100)
        entry1.place(x=400,y=100)
        password.place(x=200 , y=200)
        entry2.place(x=400,y=200)
        b = Button(root2, text="LOGIN", font="cyan",command=MyQuestion)
        b.place(x=350, y=300)
        root2.mainloop()

