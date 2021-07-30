from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ---------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generator():

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letter + password_number + password_symbols

    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD --------------------------------- #
def save_password():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
                website:
                {
                  'email' : email,
                  'password' : password
                }
               }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You left one or more fields empty")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entred\nEmail : {email}\nPassword : {password}")
        if is_ok:
            try:
                with open("password.json", 'r') as passfile:
                    data = json.load(passfile) #read old data
            except FileNotFoundError:
                with open("password.json", 'w') as passfile:
                    json.dump(new_data, passfile, indent = 4)
            else:
                data.update(new_data)
                with open("password.json", 'w') as passfile:
                    json.dump(data, passfile, indent = 4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("password.json") as passfile:
            data = json.load(passfile)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP -------------------------------------- #
## ---------------------------- Window --------------------------------------- #

window = Tk()
window.title('password generator')

## --------------------------- Image ----------------------------------------- #

img = ImageTk.PhotoImage(Image.open("logo.png"))
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100,112,image = img)
canvas.grid(row = 0,column = 1,padx = (20,20))

## --------------------------- Label ----------------------------------------- #

website = Label(text = "Website")
website.grid(row = 1,column = 0)
user = Label(text = "Username/Email")
user.grid(row = 2, column = 0)
password = Label(text = 'Password')
password.grid(row = 3, column = 0)

## --------------------------- Entry ----------------------------------------- #

website_entry = Entry(width = 21)
website_entry.focus() #add cursor
website_entry.grid(row = 1, column = 1, columnspan = 2)
user_entry = Entry(width = 35)
user_entry.insert(END, "youssef@email.com")
user_entry.grid(row = 2, column = 1, columnspan = 2)
password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1)

## -------------------------- Button ----------------------------------------- #
search = Button(text = 'Search', command = search_password)
search.grid(row = 1, column = 2)
generate = Button(text = 'Generate', command = generator)
generate.grid(row = 3, column = 2)
add = Button(text = 'Add' , width = 36,command = save_password)
add.grid(row = 4, column = 1)




window.mainloop()