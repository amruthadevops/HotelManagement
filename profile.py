from tkinter import *
from tkinter import messagebox
import os
import query2 as q

root5 = Tk()
root5.overrideredirect(1)
root5.title('login page')
root5.geometry('610x610+300+200')
root5.configure(bg="#fff")
root5.resizable(False, False)

def home():
    root5.destroy()
    os.startfile('customer.py')

def contact():
    root5.destroy()
    os.startfile('contact.py')

def room():
    root5.destroy()
    os.startfile('rooms.py')

def booking():
    root5.destroy()
    os.startfile('booking.py')

def bookdetails():
    root5.destroy()
    os.startfile('bookdetails.py')

def profile():
    root5.destroy()
    os.startfile('profile.py')

def viewprof():
    root5.destroy()
    os.startfile('viewprofile.py')

def changepass():
    root5.destroy()
    os.startfile('changepas.py')

i = q.get_login()
for data in i:
    id1=data[0]
    em=data[1]

d = q.get_book(em)
for data in d:
    name1 = data[0]
  
frame = Frame(root5, width=650, height=650, bg="white")
frame.place(x=0, y=30)


Button(root5,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root5,width=15,text="About", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root5,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root5,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root5,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root5,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

imgcus = PhotoImage(file='pro.png')
lab= Label(root5, image=imgcus, bg='white')
lab.place(x=200, y=40)

label1=Label(frame, text=name1, fg='Black', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
label1.place(x=270,y=250)

view= Button(frame,width=45, text='View Profile', border=0, bg='white', cursor='hand2', fg='#57a1f8', font=('Microsoft YaHei UI Light', 12, 'bold'), command=viewprof)
view.place(x=80, y=280)

log= Button(frame,width=45, text='change password', border=0, bg='white', cursor='hand2', fg='#57a1f8', font=('Microsoft YaHei UI Light', 12, 'bold'),command=changepass)
log.place(x=80, y=310)

log= Button(frame,width=45, text='logout', border=0, bg='white', cursor='hand2', fg='#57a1f8', font=('Microsoft YaHei UI Light', 12, 'bold'))
log.place(x=80, y=350)

root5.mainloop()
