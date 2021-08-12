"""import smtplib
msg = "subject:Hello\n\nThis is the body of the email"
my_email =  'leonabbassi@gmail.com'
my_password = 'kratos.95' 
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = my_password)
    connection.sendmail(from_addr = my_email, to_addrs = 'youssef.abbih@gmail.com',msg = msg)
"""
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
hour = now.hour
minute = now.minute
second = now.second
birth_day = dt.datetime(year = 1995, month = 6, day = 20)
#print(now)
print(day_of_week)
#print(birth_day)
