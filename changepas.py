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

def validate_pas(pa,pas):
    if pa!=pas:
        messagebox.showerror("ERROR","passwords dont match")
    else:
        d=q.update_pass(id1,pa,pas)
        if d==0:
            messagebox.showinfo("success", "password changed sucessfully, now loging out pleasere login")
            root5.destroy()
            import login

def changepas():
    pas=pas_entry.get()
    cpas=conpas_entry.get()
    validate_pas(pas,cpas)

i = q.get_login()
for data in i:
    id1=data[0]
    em=data[1]
    
  
frame = Frame(root5, width=650, height=650, bg="white")
frame.place(x=0, y=30)


Button(root5,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root5,width=15,text="About", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root5,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root5,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root5,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root5,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

pas= Label(text='Password',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
pas.place(x=150, y=180)

pas_entry = Entry(show="*",width=20,fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
pas_entry.place(x=230, y=180)

def show():
    if(sh_v.get()==1):
        pas_entry.config(show='')
    else:
        pas_entry.config(show='*')

sh_v=IntVar(value=0)

sh= Checkbutton(width=6, text='($)',variable=sh_v, border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show)
sh.place(x=400, y=180)

conpas= Label(text='Confirm Password',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
conpas.place(x=90, y=220)

conpas_entry = Entry(show="*",width=20,fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
conpas_entry.place(x=230, y=220)

def show():
    if(sh1_v.get()==1):
        conpas_entry.config(show='')
    else:
        conpas_entry.config(show='*')

sh1_v=IntVar(value=0)

sh1= Checkbutton(width=6, text='($)',variable=sh1_v, border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show)
sh1.place(x=400, y=220)

change= Button(width=16, text='change password', bg='white', cursor='hand2', fg='#57a1f8', command=changepas)
change.place(x=250, y=280)


root5.mainloop()
