from tkinter import *
from tkinter import messagebox
import tkinter as th
import os

root7 = th.Tk()
root7.overrideredirect(1)
root7.title('contact')
root7.geometry('610x610+300+200')
root7.configure(bg="#fff")
root7.resizable(False, False)

def home():
    root7.destroy()
    os.startfile('customer.py')

def contact():
    root7.destroy()
    os.startfile('contact.py')

def room():
    root7.destroy()
    os.startfile('rooms.py')

def booking():
    root7.destroy()
    os.startfile('booking.py')

def bookdetails():
    root7.destroy()
    os.startfile('bookdetails.py')

def profile():
    root7.destroy()
    os.startfile('profile.py')

  
frame1 = Frame(root7, width=650, height=650, bg="white")
frame1.place(x=0, y=30)

Button(root7,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root7,width=15,text="About", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root7,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root7,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root7,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root7,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

imgcus = PhotoImage(file='cont.png')
lab= Label(root7, image=imgcus, bg='white')
lab.place(x=110, y=40)

label1=Label(frame1, text='Address:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label1.place(x=100,y=200)

label2=Label(frame1, text='RajajiNagar, Banglore - 580009', fg='black', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label2.place(x=190,y=200)

label3=Label(frame1, text='Contact:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label3.place(x=100,y=250)

label4=Label(frame1, text='9076545894, 0821-234567', fg='black', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label4.place(x=190,y=250)

label5=Label(frame1, text='Email:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label5.place(x=100,y=300)

label6=Label(frame1, text='9076545894, 0821-234567', fg='black', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label6.place(x=190,y=300)

root7.mainloop()







