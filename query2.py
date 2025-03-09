import mysql.connector
from tkinter import messagebox




def validate_reg(row, m, p):
    res="T"
    for data in row:
        if data[0] == m or data[1] == p:
            messagebox.showerror("error",
                                 "email or phone number already used, please try with different email or phonenumber")
            res = "F"
        else:
            break
    return res


def register(n, m, p, g, a, ad, idf, idn, pa, pas):
    con = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur = con.cursor()
    cur1=con.cursor()
    query1 = "select email,ph from customer where ph='" + p + "'"
    cur.execute(query1)
    row = cur.fetchall()
    cur.close()
    res1 = validate_reg(row, m, p)



    if res1=="T":
        query2 = "INSERT INTO customer(name,email,ph,gender,age,ad,idf,idn,pas,conpas) VALUES('" + n + "','" + m + "','" + p + "','" + g + "','" + a + "','" + ad + "','" + idf + "','" + idn + "','" + pa + "','" + pas + "')"
        cur1.execute(query2)
        con.commit()
        con.close()

    return res1

def validate_prof(row, m, p):
    res="F"
    for data in row:
        if data[0] == m and data[1] == p:
            res = "T"
        else:
            break
    return res

def login(e,p):
    con1 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur2 = con1.cursor()

    query1 = "select email,pas from customer where email='" + e + "'"
    cur2.execute(query1)
    row = cur2.fetchall()
    con1.commit()
    con1.close()
    res3=validate_prof(row, e, p)
    return res3

def login_insert(e):
    con2 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur3 = con2.cursor()
    cur4 = con2.cursor()

    query = "select id from customer where email='" + e + "'"
    cur3.execute(query)
    row = cur3.fetchall()
    cur3.close()
    for data in row:
        i=str(data[0])


    query1 = "INSERT INTO login(id,email) values('"+i+"','"+e+"')"
    cur4.execute(query1)
    con2.commit()
    cur4.close()

def get_login():
    con7 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur7 = con7.cursor()


    query7 = "select id,email from login"
    cur7.execute(query7)
    row = cur7.fetchall()
    cur7.close()

    return row

def get_book(i):
    con2 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur3 = con2.cursor()
    cur4 = con2.cursor()
    val=[int(i)]

    query = "select name from customer where email='" + i + "'"
    cur3.execute("select name from customer where id=%s",val)
    row = cur3.fetchall()
    return row

def get_info(id1):
    con8 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur8 = con8.cursor()
    val = [int(id1)]
    cur4 = con8.cursor()

    cur8.execute("select name,email,ph,gender,age,ad,idf,idn from customer where id=%s",val)
    row1 = cur8.fetchall()
    con8.close()
    return row1

def update_info(id1,n,m,p,g,a,d,df,dn):
    con5 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur5 = con5.cursor()

    val=[int(id1)]
    s=cur5.execute("update customer set name='"+n+"',email='"+m+"',ph='"+p+"',gender='"+g+"',age='"+a+"',ad='"+d+"',idf='"+df+"',idn='"+dn+"' where id=%s",val)

    con5.commit()
    return 0

def update_pass(id1,p,p1):
    con5 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur5 = con5.cursor()

    val = [int(id1)]
    s = cur5.execute(
        "update customer set pas='" + p + "', conpas='" + p1 + "' where id=%s",
        val)

    con5.commit()
    return 0

def val_book(res5,ch,co):
    m="T"
    for data in res5:
        if str(data[0])==ch and str(data[1])==co:
            messagebox.showerror("error","you have already booked for selected date please slect other dates")
            m="F"
        else:
            break

    return m

def insert_book(idn,n,r,rn,ci,co,ni,am):
    con9 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur9 = con9.cursor()
    cur10= con9.cursor()
    s="not confirmed"
    val=[int(idn)]


    cur10.execute("select chin,chou from booking where id=%s",val)
    res4=cur10.fetchall()
    m=val_book(res4,ci,co)

    if m=="T":
        query9="INSERT INTO booking(id,name,room,non,chin,chou,nod,am,status) VALUES('" + idn + "','" + n + "','" + r + "','" + rn + "','" + ci + "','" + co + "','" + ni + "','" + am + "','"+s+"')"
        cur9.execute(query9)
        con9.commit()

    return m


def get_booking(id):
    con10 = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cur11 = con10.cursor()
    cur4 = con10.cursor()
    val = [int(id)]


    cur11.execute("select room,non,chin,chou,nod,am,status from booking where id=%s", val)
    row9= cur11.fetchall()
    return row9
