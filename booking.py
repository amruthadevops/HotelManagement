from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import date
import os
import query2 as q

today = date.today()
root3 = Tk()
root3.overrideredirect(1)
root3.title('contact')
root3.geometry('610x610+300+200')
root3.configure(bg="#fff")
root3.resizable(False, False)



def home():
    root3.destroy()
    os.startfile('customer.py')

def contact():
    root3.destroy()
    os.startfile('contact.py')

def room():
    root3.destroy()
    os.startfile('rooms.py')

def booking():
    root3.destroy()
    os.startfile('booking.py')

def bookdetails():
    root3.destroy()
    os.startfile('bookdetails.py')

def profile():
    root3.destroy()
    os.startfile('profile.py')

def val(idn,n,r,rn,ci,co,nod,am):
    if idn=="" or n=="" or r=="" or rn=="" or ci=="" or co=="" or am=="" or nod=="":
        messagebox.showerror("ERROR","Fields cannot be Blank")
    else:
        sd=q.insert_book(idn,n,r,rn,ci,co,nod,am)
        if sd=="T":
            messagebox.showinfo("sucesss", "room has been booked")
            root3.destroy()
            os.startfile('customer.py')



def calc():
    num=0
    ch=0
    ch0=0
    ch=cal.get_date()
    ch0=cal1.get_date()
    num= (ch0-ch).days
    noro_entry.insert(0,num)
    noro_entry.config(state="normal")
    noro_entry.delete(0, END)
    noro_entry.insert(0, num)
    noro_entry.config(state="disable")

    sig= 1500
    dob=2000
    delux=2500
    NonACsingle=700
    NonACDouble=1000
    BigRoom=3000

    if menu1.get()=="A\C single room":
        amoun = int(num * sig)
        amount_entry.config(state="normal")
        amount_entry.delete(0, END)
        amount_entry.insert(0, amoun)
        amount_entry.config(state="disable")
        non_entry.config(state="normal")
        non_entry.delete(0, END)
        non_entry.insert(0, "1")
        non_entry.config(state="disable")
    elif menu1.get()=="A\C Double room":
         amoun = int(num * dob)
         amount_entry.config(state="normal")
         amount_entry.delete(0, END)
         amount_entry.insert(0, amoun)
         amount_entry.config(state="disable")
         non_entry.config(state="normal")
         non_entry.delete(0, END)
         non_entry.insert(0, "2")
         non_entry.config(state="disable")
    elif menu1.get()=="delux room":
          amoun = int(num * delux)
          amount_entry.config(state="normal")
          amount_entry.delete(0, END)
          amount_entry.insert(0, amoun)
          amount_entry.config(state="disable")
          non_entry.config(state="normal")
          non_entry.delete(0, END)
          non_entry.insert(0, "2")
          non_entry.config(state="disable")
    elif menu1.get()=="Non A\C single room":
          amoun = int(num * NonACsingle)
          amount_entry.config(state="normal")
          amount_entry.delete(0, END)
          amount_entry.insert(0, amoun)
          amount_entry.config(state="disable")
          non_entry.config(state="normal")
          non_entry.delete(0, END)
          non_entry.insert(0, "1")
          non_entry.config(state="disable")
    elif menu1.get()=="Non A\C Double room":
          amoun = int(num * NonACDouble)
          amount_entry.config(state="normal")
          amount_entry.delete(0, END)
          amount_entry.insert(0, amoun)
          amount_entry.config(state="disable")
          non_entry.config(state="normal")
          non_entry.delete(0, END)
          non_entry.insert(0, "2")
          non_entry.config(state="disable")
    elif menu1.get()=="Big Room":
          amoun = int(num * BigRoom)
          amount_entry.config(state="normal")
          amount_entry.delete(0, END)
          amount_entry.insert(0, amoun)
          amount_entry.config(state="disable")
          non_entry.config(state="normal")
          non_entry.delete(0, END)
          non_entry.insert(0, "max 4")
          non_entry.config(state="disable")
        
           

def bookt():
    idn=id_entry.get()
    name= name_entry.get()
    ro= menu1.get()
    noper= non_entry.get()
    amoun=amount_entry.get()
    chein=cal.get()
    cheou=cal1.get()
    nod=noro_entry.get()
    val(idn,name,ro,noper,chein,cheou,nod,amoun)


i = q.get_login()
for data in i:
    id1=data[0]
    em=data[1]

d = q.get_book(id1)
for data1 in d:
    name1 = data1[0]


    
  
frame = Frame(root3, width=650, height=650, bg="white")
frame.place(x=0, y=30)

Button(root3,width=15,text="Home", pady=7, bg='#57a1f8', fg='white', border=0, command=home).place(x=0, y=0)
Button(root3,width=15,text="About", pady=7, bg='#57a1f8', fg='white', border=0,command=room).place(x=80, y=0)
Button(root3,width=15,text="Booking", pady=7, bg='#57a1f8', fg='white', border=0,command=booking).place(x=160, y=0)
Button(root3,width=17,text="Booking details", pady=7, bg='#57a1f8', fg='white', border=0,command=bookdetails).place(x=270, y=0)
Button(root3,width=15,text="Contact us", pady=7, bg='#57a1f8', fg='white', border=0, command=contact).place(x=390, y=0)
Button(root3,width=15,text="profile", pady=7, bg='#57a1f8', fg='white', border=0,command=profile).place(x=500, y=0)

heading = Label(text='BOOK ROOM', fg='blue', bg='white', font=('Microsoft YaHei UI Light', 15, 'bold'))
heading.place(x=250, y=50)

id= Label(text='ID Number',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
id.place(x=200, y=90)

id_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
id_entry.place(x=300, y=90)
id_entry.insert(0, id1)
id_entry.config(state= "disabled")

name= Label(text='Name',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
name.place(x=200, y=120)

name_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
name_entry.place(x=300, y=120)
name_entry.insert(0,name1)
name_entry.config(state= "disabled")

room= Label(text='Room',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
room.place(x=200, y=160)

rom=["A\C single room","A\C Double room", "delux room","Non A\C single room","Non A\C Double room","Big Room"]
menu1= StringVar()
menu1.set("select Room")
drop1=OptionMenu(root3,menu1,*rom).place(x=300,y=160)

non= Label(text='No of person',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
non.place(x=200, y=200)

non_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
non_entry.place(x=300, y=200)
non_entry.config(state= "disabled")


checkin= Label(text='Checkin',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
checkin.place(x=200, y=230)

cal=DateEntry(root3,mindate=today, width=15,fg='black', bg='white',bd=2)
cal.place(x=300,y=240)

checkout= Label(text='Checkout',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
checkout.place(x=200, y=270)

cal1=DateEntry(root3,mindate=today, width=15,fg='black', bg='white',bd=2)
cal1.place(x=300,y=270)

calc= Button(width=6, text='(cal)',border=0, bg='white', cursor='hand2', fg='#57a1f8', command=calc)
calc.place(x=450, y=270)

noro= Label(text='No of Days',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
noro.place(x=200, y=300)

noro_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
noro_entry.place(x=300, y=300)
noro_entry.config(state= "disabled")

amount= Label(text='Amount',fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
amount.place(x=200, y=330)

amount_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
amount_entry.place(x=300, y=330)
amount_entry.config(state= "disabled")

book= Button(width=6, text='book', bg='white', cursor='hand2', fg='#57a1f8', command=bookt)
book.place(x=300, y=390)

root3.mainloop()
