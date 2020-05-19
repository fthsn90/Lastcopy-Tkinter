#Coded by fthsn90 
#20.05.2020
from tkinter import *
import tkinter
import win32clipboard
from tkinter import messagebox

class kopici:
    def __init__(self):
        self.sayi = 1
        self.root = Tk()
        self.root.title("Mycopies")
        self.root.geometry("400x400")
        self.frame = Frame(self.root)
        self.dikey = Scrollbar(self.root,orient = VERTICAL)
        self.dikey.pack(side=RIGHT,fill=Y)
        self.app()
        self.dikey.config(command=self.txt.yview)
        self.root.mainloop()

    def app(self):
        self.txt = Text(self.frame,width=40,height=20,bd=2)
        self.txt.grid(row=0,column=0)
        self.button = Button(self.frame,text="Get Copy",command=self.cek,bd=3)
        self.button.grid()
        self.button2 = Button(self.frame,text="Save",command=self.kaydet,bd=3)
        self.button2.grid()
        self.frame.pack()
    
    def cek(self):
        self.number = self.root.clipboard_get()
        self.txt.insert(END,"{}. {}\n".format(self.sayi,self.number))
        self.sayi +=1

    def kaydet(self):
        with open("copies.txt","a") as f:
            f.write("{}".format(self.txt.get(1.0,END)))
            messagebox.showinfo("Info","Copies saved.")



kopici()