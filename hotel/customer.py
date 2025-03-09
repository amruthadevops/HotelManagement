from tkinter import *
from tkinter import messagebox
import os



root = Tk()
root.overrideredirect(1)
root.title('login page')
root.geometry('610x610+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def home():
    root.destroy()
    os.startfile('customer.py')

def contact():
    root.destroy()
    os.startfile('contact.py')

def room():
    root.destroy()
    os.startfile('rooms.py')

def booking():
    root.destroy()
    os.startfile('booking.py')

def bookdetails():
    root.destroy()
    os.startfile('bookdetails.py')

def profile():
    root.destroy()
    os.startfile('profile.py')
  
frame = Frame(root, width=650, height=650, bg="white")
frame.place(x=0, y=30)

img = PhotoImage(file='hotel4.png')
Label(frame, image=img, bg='white').place(x=200, y=120)

Button(root,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root,width=15,text="Rooms", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

frame = Frame(root, width=650, height=650, bg="white")
frame.place(x=0, y=30)

img = PhotoImage(file='hotel4.png')
Label(frame, image=img, bg='white').place(x=200, y=120)


label=Label(frame, text='Hotel management project provides room booking and other necessary hotel management features', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 8, 'bold'))
label.place(x=0,y=0)

root.mainloop()




