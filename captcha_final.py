from tkinter import *
from tkinter import messagebox
import tkinter
import random
import sqlite3

root=tkinter.Tk()

def entry():
    global cursor
    cap=sqlite3.connect('Database1.db')
    cursor=cap.cursor() #cursor is used for a connection with database
    cursor.execute('CREATE TABLE IF NOT EXISTS Entry(regno int)')
    cursor.execute('INSERT INTO Entry VALUES(?)',(regno.get()))
    cap.commit() #to make the changes permanent
    cursor.close()

code=''

def generate():
    p=''
    global result
    global a
    global h
    h=[]
    for i in range(0,3):
        if i==1: #for generation of operators
            value=random.choice(['+','-','*','/'])
            p+=value
            h.append(value)
        elif i==0: #for generation of digits
            value=random.randint(1,9)
            d=(value) #storing 'value' in 'd' and appending in h afterwards
            p+=str(value)
            h.append(d)
        else: #generation of digits
            value=random.randint(1,6)
            p+=str(value)
            h.append(value)

    a=h
    return p

def check(): #for checking whether the values are correct or not
    ck=ent_cap.get()
    ent_cap.delete(0,END) # for ending the session
    r=reg_no.get()
    global abc
    if(r.isdigit() and (len(r)==8 or len(r)==5)):
        rgn=reg_no.get()
    else:
        messagebox.showinfo("ERROR","Invalid Registration number")
        reg_no.delete(0,END)
        return 0

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a//b

    
    aa=h[1]
    if aa=='+':
        op=add
    elif aa=='-':
        op=sub
    elif aa=='*':
        op=mul
    elif aa=='/':
        op=div
    result=op(h[0],h[2])

    if ck==str(result):
        messagebox.showinfo("ACCESS","You have successfully registered")
        entry()
        exit
    else:
        messagebox.showinfo("ERROR","Wrong answer")
        g=generate()
        display()
        c.create_text(160,40,text=g,font="Calibri 32 bold")
        c.grid(row=3,column=10)


def display():
    c.create_rectangle(80,10,240,70,fill="white")
    c.create_line(80,20,230,50)
    c.create_line(85,55,180,25)
    c.create_line(150,10,170,70)
    c.create_line(100,65,240,40)


def reset():
    ent_cap.delete(0,END)
    global code
    g=generate()
    code=g
    display()
    c.create_text(160,40,text=g,font='Calibri 30 bold')
    c.grid(row=3,column=10)

code=generate()
abc=[]
reg=tkinter.Label(root,text='Enter registration number ',font='Times 20')
reg.grid(row=1,column=10)
reg_no=Entry(root)
reg_no.grid(row=1,column=11)
root.geometry('450x220')
root.title("PASSWORD REMINDER")
img1=PhotoImage(file="na.png")
a=Canvas(root,height=450,width=220,bg='red')
c=Canvas(root,height=80,width=240)
display()
c.create_text(160,40,text=code,font='Calibri 28 bold')
c.grid(row=3,column=10)
l1=tkinter.Label(root,text='Your answer',font='Calibri 30 bold')
l1.grid(row=5,column=10)
ent_cap=Entry(root)
ent_cap.grid(row=6,column=10)
sbutton=tkinter.Button(root,text='Submit',command=check,height=1,width=10)
sbutton.grid(row=9,column=10)
img1=PhotoImage(file='na.png')
reset1=tkinter.Button(root,text='Reload',height=72,width=72,image=img1,command=reset)
reset1.grid(row=3,column=11)
root.mainloop()

