import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
if now.weekday() == 0:
    with open('quotes.txt') as quotes:
        quotes.readline()
        quotes = [quote.strip() for quote in quotes]

    msg = f"subject:Quote of the day\n\n{choice(quotes)}"
    my_email =  'leonabbassi@gmail.com'
    my_password = 'kratos.95' 
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = my_password) 
        connection.sendmail(from_addr = my_email, to_addrs = 'youssef.abbih@gmail.com',msg = msg)
