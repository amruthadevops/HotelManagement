from tkinter import *
from tkinter import messagebox
import query2 as q1
import re
import mail as ms


root = Tk()
# root.overrideredirect(1)
root.title('login page')
root.geometry('500x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


def val(n, m, p, g, a, ad, idf, idn, pa, pas):
    if n == "" or m == "" or p == "" or g == "" or a == "" or ad == "" or idf == "" or idn == "" or pa == "" or pas == "":
        messagebox.showerror("ERROR", "Fields cannot be Blank")
    else:
        validate_name(n, m, p, g, a, ad, idf, idn, pa, pas)


def validate_name(n, m, p, g, a, ad, idf, idn, pa, pas):
    if (n.isalpha()):
        validate_email(n, m, p, g, a, ad, idf, idn, pa, pas)
    else:
        messagebox.showerror("ERROR", "invalid Name")


def validate_email(n, m, p, g, a, ad, idf, idn, pa, pas):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(pattern, m)):
        validate_ph(n, m, p, g, a, ad, idf, idn, pa, pas)
    else:
        messagebox.showerror("ERROR", "invalid email")


def validate_ph(n, m, p, g, a, ad, idf, idn, pa, pas):
    r = re.fullmatch('[6-9][0-9]{9}', p)
    if r != None:
        validate_age(n, m, p, g, a, ad, idf, idn, pa, pas)
    else:
        messagebox.showerror("ERROR", "invalid Phone Number")


def validate_age(n, m, p, g, a, ad, idf, idn, pa, pas):
    r = re.fullmatch('[1-9]{2}', a)
    if r != None and int(a) <= 100:
        validate_pas(n, m, p, g, a, ad, idf, idn, pa, pas)
    else:
        messagebox.showerror("ERROR", "invalid age")


def validate_pas(n, m, p, g, a, ad, idf, idn, pa, pas):
    if pa != pas:
        messagebox.showerror("ERROR", "passwords dont match")
    else:
        register(n, m, p, g, a, ad, idf, idn, pa, pas)

def register(n, m, p, g, a, ad, idf, idn, pa, pas):
    qa=q1.register(n, m, p, g, a, ad, idf, idn, pa, pas)
    if qa=="T":
        messagebox.showinfo("sucess", "register sucessfully")
        fullname_entry.delete(0, END)
        email_entry.delete(0, END)
        Phone_entry.delete(0, END)
        age_entry.delete(0, END)
        add_entry.delete(0, END)
        idno_entry.delete(0, END)
        pas_entry.delete(0, END)
        conpas_entry.delete(0, END)


def signup():
    name = fullname_entry.get()
    mail = email_entry.get()
    ph = Phone_entry.get()
    gen = menu1.get()
    ag = age_entry.get()
    ad = add_entry.get()
    idf = menu.get()
    idn = idno_entry.get()
    pas = pas_entry.get()
    cpas = conpas_entry.get()
    val(name, mail, ph, gen, ag, ad, idf, idn, pas, cpas)


heading = Label(text='SING UP', fg='blue', bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
heading.place(x=180, y=5)

fullname = Label(text='FullName', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
fullname.place(x=100, y=60)

fullname_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
fullname_entry.place(x=190, y=60)

email = Label(text='Email', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
email.place(x=100, y=90)

email_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
email_entry.place(x=190, y=90)

phone = Label(text='Phone Number', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
phone.place(x=40, y=120)

Phone_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
Phone_entry.place(x=190, y=120)

gender = Label(text='Gender', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
gender.place(x=100, y=170)

gen = ["Male", "Female", "Others"]
menu1 = StringVar()
menu1.set("select gender")
drop1 = OptionMenu(root, menu1, *gen).place(x=190, y=170)

age = Label(text='Age', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
age.place(x=100, y=200)

age_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
age_entry.place(x=190, y=200)

add = Label(text='Address', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
add.place(x=100, y=230)

add_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
add_entry.place(x=190, y=230)

id = Label(text='ID proof', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
id.place(x=100, y=270)

idpr = ["Adhaar", "Voter ID", "Driving Lisence", "PAN"]
menu = StringVar()
menu.set("select id proof")
drop = OptionMenu(root, menu, *idpr).place(x=190, y=270)

idno = Label(text='ID Number', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
idno.place(x=100, y=300)

idno_entry = Entry(width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
idno_entry.place(x=190, y=300)

pas = Label(text='Password', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
pas.place(x=100, y=330)

pas_entry = Entry(show="*", width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
pas_entry.place(x=190, y=330)


def show():
    if (sh_v.get() == 1):
        pas_entry.config(show='')
    else:
        pas_entry.config(show='*')


sh_v = IntVar(value=0)

sh = Checkbutton(width=6, text='($)', variable=sh_v, border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show)
sh.place(x=350, y=330)

conpas = Label(text='Confirm Password', fg='black', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
conpas.place(x=40, y=370)

conpas_entry = Entry(show="*", width=20, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
conpas_entry.place(x=190, y=370)


def show():
    if (sh1_v.get() == 1):
        conpas_entry.config(show='')
    else:
        conpas_entry.config(show='*')


sh1_v = IntVar(value=0)

sh1 = Checkbutton(width=6, text='($)', variable=sh1_v, border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show)
sh1.place(x=350, y=370)

sign_up = Button(width=10, text='sign Up', bg='white', cursor='hand2', fg='#57a1f8', command=signup)
sign_up.place(x=180, y=420)

label = Label(text="Already have as Account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=100, y=450)


def signin():
    root.destroy()
    import login


sign_in = Button(width=6, text='sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signin)
sign_in.place(x=250, y=450)

root.mainloop()
