from tkinter import *
from tkinter import messagebox
import re
import os
import query2 as q


root = Tk()
#root.overrideredirect(1)
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

def val(id1,name,mail,ph,gen,ag,ad,idf,idn):
    if name=="" or mail=="" or p=="" or g=="" or a=="" or ad=="" or idf=="" or idn=="":
        messagebox.showerror("ERROR","Fields cannot be Blank")
    else:
        validate_name(id1,name,mail,ph,gen,ag,ad,idf,idn)

def validate_name(id1,name,mail,ph,gen,ag,ad,idf,idn):
    if(name.isalpha()):
        validate_email(id1,name,mail,ph,gen,ag,ad,idf,idn)
    else:
         messagebox.showerror("ERROR","invalid Name")

def validate_email(id1,name,mail,ph,gen,ag,ad,idf,idn):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(pattern,mail)):
        validate_ph(id1,name,mail,ph,gen,ag,ad,idf,idn)
    else:
        messagebox.showerror("ERROR","invalid email")

def validate_ph(id1,name,mail,ph,gen,ag,ad,idf,idn):
    r=re.fullmatch('[6-9][0-9]{9}',ph)
    if r!=None:
        validate_age(id1,name,mail,ph,gen,ag,ad,idf,idn)
    else:
        messagebox.showerror("ERROR","invalid Phone Number")

def validate_age(id1,name,mail,ph,gen,ag,ad,idf,idn):
    r=re.fullmatch('[1-9]{2}',ag)
    if r!=None and int(ag)<=100:
        s=q.update_info(id1,name,mail,ph,gen,ag,ad,idf,idn)
        if s==0:
            messagebox.showinfo("success","information updated" )
            fullname_entry.config(state="disable")
            email_entry.config(state="disable")
            Phone_entry.config(state="disable")
            age_entry.config(state="disable")
            add_entry.config(state="disable")
            idno_entry.config(state="disable")
            update1.config(state="disable")
            update.config(state="normal")
    else:
         messagebox.showerror("ERROR","invalid age")

def upadateprofile():
    fullname_entry.config(state="normal")
    email_entry.config(state="normal")
    Phone_entry.config(state="normal")
    age_entry.config(state="normal")
    add_entry.config(state="normal")
    idno_entry.config(state="normal")
    update1.config(state="normal")
    update.config(state="disable")

def update2():
    name=fullname_entry.get()
    mail=email_entry.get()
    ph=Phone_entry.get()
    gen=menu1.get()
    ag=age_entry.get()
    ad=add_entry.get()
    idf=menu.get()
    idn=idno_entry.get()
    val(id1,name,mail,ph,gen,ag,ad,idf,idn)
    
    
    

    
frame1 = Frame(root, width=650, height=650, bg="white")
frame1.place(x=0, y=30)

Button(root,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root,width=15,text="About", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

i = q.get_login()
for data in i:
    id1=data[0]
    em=data[1]

info= q.get_info(id1)
for data1 in info:
    nan=data1[0]
    e=data1[1]
    p=data1[2]
    g=data1[3]
    a=data1[4]
    ad=data1[5]
    idp=data1[6]
    idn=data1[7]
    break

fullname= Label(text='FullName',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
fullname.place(x=100, y=60)

fullname_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
fullname_entry.place(x=190, y=60)
fullname_entry.insert(0,nan)
fullname_entry.config(state="disable")


email= Label(text='Email',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
email.place(x=100, y=90)

email_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
email_entry.place(x=190, y=90)
email_entry.insert(0,e)
email_entry.config(state="disable")


phone= Label(text='Phone Number',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
phone.place(x=40, y=120)

Phone_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
Phone_entry.place(x=190, y=120)
Phone_entry.insert(0,p)
Phone_entry.config(state="disable")


gender= Label(text='Gender',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
gender.place(x=100, y=170)

gen=["Male","Female", "Others"]
menu1= StringVar()
menu1.set(g)
drop1=OptionMenu(root,menu1,*gen).place(x=190,y=170)

age= Label(text='Age',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
age.place(x=100, y=200)

age_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
age_entry.place(x=190, y=200)
age_entry.insert(0,a)
age_entry.config(state="disable")


add= Label(text='Address',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
add.place(x=100, y=230)

add_entry = Entry(width=20,fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
add_entry.place(x=190, y=230)
add_entry.insert(0,ad)
add_entry.config(state="disable")

id= Label(text='ID proof',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
id.place(x=100, y=270)

idpr=["Adhaar","Voter ID", "Driving Lisence", "PAN"]
menu= StringVar()
menu.set(idp)
drop=OptionMenu(root,menu,*idpr).place(x=190,y=270)

idno= Label(text='ID Number',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
idno.place(x=100, y=300)

idno_entry = Entry(width=20,fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
idno_entry.place(x=190, y=300)
idno_entry.insert(0,idn)
idno_entry.config(state="disable")

update= Button(width=10, text='update profile?', bg='white', cursor='hand2', fg='#57a1f8', command=upadateprofile)
update.place(x=150, y=340)

update1= Button(width=10, text='update', bg='white', cursor='hand2', fg='#57a1f8', command=update2)
update1.place(x=280, y=340)
update1.config(state="disable")


root.mainloop()



