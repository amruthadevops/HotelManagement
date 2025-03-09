import smtplib, ssl

port=465

context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
    server.login("admin@gmail.com","admin")
    server.sendmail("admin@gmail.com","admin@gmail.com","hi")


