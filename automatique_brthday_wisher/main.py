import smtplib
import pandas as pd
import numpy as np
import datetime as dt
from random import randint

# TODO1 Update the birthdays.csv
# TODO2 Check if today matches a birthday in the birthdays.csv
# TODO3 If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# TODO4 Send the letter generated in step 3 to that person's email address.'

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
txt = "[NAME]"

def add_row():
    person = {}
    persons = []
    end = False
    while not end:
        info = input('do you want to add a person Y or N ').upper()
        if info == 'N':
            end = True
        else:
            person['name']  = input('Enter the name ')
            person['email'] = input('Enter the email ')
            person['year']  = int(input('Enter the year '))
            person['month'] = int(input('Enther the month '))
            person['day']   = int(input('Enter the day '))
    if person:
       persons.append(person)

    else:
        pass
    return persons

def check_date(df, year=year, month = month, day = day):
    exist = month in df['month'].values and day in df['day'].values
    if exist:
        with open(f'letter_templates/letter_{randint(1,3)}.txt') as letter:
            wish= letter.read()
            name = df[((df['month'] == month) & (df['day'] == day))]['name'].values[0]
            wish_birth = wish.replace(txt,name)
            print(wish_birth)
    return wish_birth
def send_email(msg):
    msg = f"subject:Happy BirthDay\n\n{msg}"
    my_email =  'leonabbassi@gmail.com'
    my_password = 'kratos.95' 
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = my_password) 
        connection.sendmail(from_addr = my_email, to_addrs = 'youssef.abbih@gmail.com',msg = msg)


birthdays = pd.read_csv('birthdays.csv')
birthdays.dropna(axis = 0, inplace = True)
birthdays = birthdays.astype({'year':int, 'month' : int, 'day' : int})
birthdays = birthdays.append(add_row(),ignore_index  = True)
print(birthdays)
birthdays.to_csv('birthdays.csv', index = False)
msg = check_date(birthdays,month = month, day = day)
send_email(msg)

