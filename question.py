from tkinter import *
import PyMySQL

class MyQuestion:
    def btn_s1(self):
        db = PyMySQL.connect("localhost", "root", "root123", "MockExam")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print("Database version : %s " % data)

        # disconnect from server
        db.close()
    def __init__(self):
        root4=Tk()
        root4.title("QUESTION")
        l=Label(root4,text="QUESTIONS")
        l.place(x=650,y=5)
        root4.geometry("1500x1500")
        s1=Button(root4, text="ADD", command=self.btn_s1())
        s1.place(x=500, y=50, width=50, height=20)
        s2= Button(root4,text="DELETE")
        s2.place(x=600, y=50, width=50, height=20)
        s3= Button(root4,text="DONE")
        s3.place(x=700,y=50,width=50,height=20)
        root4.mainloop()