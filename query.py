import mysql.connector
from tkinter import messagebox


def register(n, m, p, g, a, ad, idf, idn, pa, pas):
    query2 = "INSERT INTO customer(name,email,ph,gender,age,ad,idf,idn,pas,conpas) VALUES('" + n + "','" + m + "','" + p + "','" + g + "','" + a + "','" + ad + "','" + idf + "','" + idn + "','" + pa + "','" + pas + "')"
    cursor.execute(query2)
    return 0


def val_reg(m, p):
    connect = mysql.connector.connect(host="localhost", user="root", password="Amrutha@1992", database="hotel")
    cursor = connect.cursor()
    query1 = "select email,ph from customer where ph='" + p + "'"
    cursor.execute(query1)
    row = cursor.fetchall()
    connect.close()
    return row


