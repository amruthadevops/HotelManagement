from tkinter import *
from tkinter import messagebox
import os
import query2 as q

root4 = Tk()
root4.overrideredirect(1)
root4.title('login page')
root4.geometry('610x610+300+200')
root4.configure(bg="#fff")
root4.resizable(False, False)

def home():
    root4.destroy()
    os.startfile('customer.py')

def contact():
    root4.destroy()
    os.startfile('contact.py')

def room():
    root4.destroy()
    os.startfile('rooms.py')

def booking():
    root4.destroy()
    os.startfile('booking.py')

def bookdetails():
    root4.destroy()
    os.startfile('bookdetails.py')

def profile():
    root4.destroy()
    os.startfile('profile.py')
  
frame = Frame(root4, width=650, height=650, bg="white")
frame.place(x=0, y=50)


Button(root4,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root4,width=15,text="About", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root4,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root4,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root4,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root4,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

i = q.get_login()
for data in i:
    id1=data[0]
    em=data[1]

lis=q.get_booking(id1)

i=0
for bo in lis:
    for j in range(len(bo)):
        e = Entry(frame, width=14, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, bo[j])
    i=i+1


root4.mainloop()
