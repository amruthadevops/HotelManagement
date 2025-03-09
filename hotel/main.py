from tkinter import *


root = Tk()
root.overrideredirect(1)
root.title('main')
root.geometry('550x400+200+200')
root.configure(bg="#fff")
root.resizable(False, False)


def page():
    root.destroy()
    import login


img = PhotoImage(file='hotel3.png')
img1 = PhotoImage(file='hotel.png')
Label(root, width=300, height=200, image=img, bg='white').place(x=120, y=50)
Label(root, width=500, height=150, image=img1, bg='white').place(x=50, y=250)

root.after(4000,lambda : page())

root.mainloop()


