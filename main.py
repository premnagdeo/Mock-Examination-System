from tkinter import *
from admin import *
from student import *
import PyMySQL

root=Tk()
root.title("MOCK TEST")
root.geometry("500x500")
b1=Button(root,text="ADMIN",font="cyan",command=MyAdmin)
#b1.bind('<Button-1>',MyAdmin)
b2=Button(root,text="STUDENT",font="cyan",command=MyStudent)
#b2.bind('<Button-2>',MyStudent)
#b3=Button(root,text="RESULT",font="cyan",command)
b1.place(x=100,y=100,width=100,height=100)
b2.place(x=300,y=100,width=100,height=100)
root.mainloop()