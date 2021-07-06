import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import choice
BACKGROUND_COLOR = "#B1DDC6"



# ---------------------------- DATA SETUP -------------------------------------- #
df = pd.read_csv('data/french_words.csv')
df.to_dict(orient="records")


def next_word():
	word = choice(df['French'])
	canvas.itemconfig(card_title, text="French")
	canvas.itemconfig(card_word, text=word)
	window.after(3000)
	canvas.itemconfig(card_front, image = card_back)
# ---------------------------- UI SETUP -------------------------------------- #
## ---------------------------- Window --------------------------------------- #

window = Tk()
window.title('Flash Card')
window.configure(bg=BACKGROUND_COLOR )

## --------------------------- Image ----------------------------------------- #

card_back  = ImageTk.PhotoImage(Image.open("images/card_back.png"))
card_front = ImageTk.PhotoImage(Image.open("images/card_front.png"))
right      = ImageTk.PhotoImage(Image.open("images/right.png"))
wrong      = ImageTk.PhotoImage(Image.open("images/wrong.png"))
canvas     = Canvas(width = 800, height = 526)
canvas.create_image(400,263,image = card_front)
canvas.create_image(400,263,image = card_back)
card_title = canvas.create_text(400, 150, text = '', font = ("Arial", 40, "italic"))
card_word  = canvas.create_text(400, 263, text = '', font = ("Arial", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR)
canvas.grid(row = 0,column = 1,padx = (50,50))

## --------------------------- Label ----------------------------------------- #

## --------------------------- Entry ----------------------------------------- #



## -------------------------- Button ----------------------------------------- #

unknown_button = Button(image = wrong,highlightthickness = 0, command = next_word)
unknown_button.grid(row = 1,column = 0,padx = (50,50))
right_button = Button(image = right,highlightthickness = 0, command = next_word)
right_button.grid(row = 1,column = 2,padx = (50,50))

next_word()
window.mainloop()

