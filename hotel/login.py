from tkinter import *
from tkinter import messagebox
import query2 as q

root = Tk()
root.overrideredirect(1)
root.title('login page')
root.geometry('920x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

#pas=PhotoImage(file='pass.png')
img = PhotoImage(file='D:\\hotel\\login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def signin():
    em=user.get()
    pas=password.get()
    r=q.login(em,pas)
    if r=="T":
        q.login_insert(em)
        root.destroy()
        import customer


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Email')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Email')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)



def on_enter(e):
    password.delete(0, 'end')
    password.config(show="*")


def on_leave(e):
    name = password.get()
    if name == '':
        password.config(show="")
        password.insert(0, 'password')

def show():
    if(sh_v.get()==1):
        password.config(show='')
    else:
        password.config(show='*')

password = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, "password")
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

sh_v=IntVar(value=0)

sh= Checkbutton(frame,width=6, text='($)',variable=sh_v, border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show)
sh.place(x=300, y=150)



Button(frame, width=39,text="sign In", pady=7, bg='#57a1f8', fg='white', border=0,command=signin).place(x=35, y=204)
label=Label(frame, text="don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75,y=270)

def signup():
    root.destroy()
    import register

sign_up= Button(frame,width=6, text='sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup)
sign_up.place(x=215, y=270)

root.mainloop()
