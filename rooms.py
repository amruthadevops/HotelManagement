from tkinter import *
from tkinter import messagebox
import os

root2 = Tk()
root2.overrideredirect(1)
root2.title('contact')
root2.geometry('610x610+300+200')
root2.configure(bg="#fff")
root2.resizable(False, False)

def home():
    root2.destroy()
    os.startfile('customer.py')

def contact():
    root2.destroy()
    os.startfile('contact.py')

def room():
    root2.destroy()
    os.startfile('rooms.py')

def booking():
    root2.destroy()
    os.startfile('booking.py')

def bookdetails():
    root2.destroy()
    os.startfile('bookdetails.py')

def profile():
    root2.destroy()
    os.startfile('profile.py')
  
frame = Frame(root2, width=650, height=650, bg="white")
frame.place(x=0, y=30)

Button(root2,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root2,width=15,text="About", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root2,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root2,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root2,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root2,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

img = PhotoImage(file='room.png')
Label(frame, image=img, bg='white').place(x=0, y=10)


label1=Label(frame, text='A\C single room', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label1.place(x=300,y=10)

label2=Label(frame, text='A\C Double room', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label2.place(x=300,y=40)

label3=Label(frame, text='delux room', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label3.place(x=300,y=70)

label4=Label(frame, text='Non A\C single room', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label4.place(x=300,y=100)

label5=Label(frame, text='Non A\C Double room', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label5.place(x=300,y=130)

img1 = PhotoImage(file='faci.png')
Label(frame, image=img1, bg='white').place(x=0, y=300)

label0=Label(frame, text='Dinning', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label0.place(x=300,y=280)

label6=Label(frame, text='Internet', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label6.place(x=300,y=320)

label7=Label(frame, text='Swimming Pool', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label7.place(x=300,y=360)

label8=Label(frame, text='Garden', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label8.place(x=300,y=400)

label9=Label(frame, text='Taxis', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label9.place(x=300,y=440)


root2.mainloop()
