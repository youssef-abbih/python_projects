import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
word = {}
to_learn = {}
# ---------------------------- DATA SETUP -------------------------------------- #
try:

    df = pd.read_csv('data/words_to_learn.csv')

except FileNotFoundError:
	
	original_df = pd.read_csv('data/french_words.csv')
	to_learn = original_df.to_dict(orient="records")

else:
	
	to_learn = df.to_dict(orient="records")


def next_word():
	global word, flip_timer
	word = choice(to_learn)
	window.after_cancel(flip_timer)
	canvas.itemconfig(card_title, text="French", fill = "black")
	canvas.itemconfig(card_word, text=word['French'], fill = 'black')
	canvas.itemconfig(card_background, image = card_front)
	flip_timer = window.after(3000,func = flip_card)

def flip_card():
	canvas.itemconfig(card_title, text="English", fill = "white")
	canvas.itemconfig(card_word, text=word['English'], fill = "white")
	canvas.itemconfig(card_background, image = card_back)
def is_known():
    to_learn.remove(word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()
# ---------------------------- UI SETUP -------------------------------------- #
## ---------------------------- Window --------------------------------------- #

window = Tk()
window.title('Flash Card')
window.configure(bg=BACKGROUND_COLOR )
flip_timer = window.after(3000,func = flip_card)

## --------------------------- Image ----------------------------------------- #

card_back        = ImageTk.PhotoImage(Image.open("images/card_back.png"))
card_front       = ImageTk.PhotoImage(Image.open("images/card_front.png"))
right            = ImageTk.PhotoImage(Image.open("images/right.png"))
wrong            = ImageTk.PhotoImage(Image.open("images/wrong.png"))
canvas           = Canvas(width = 800, height = 526)
card_background  = canvas.create_image(400,263,image = card_front)
card_title       = canvas.create_text(400, 150, text = '', font = ("Arial", 40, "italic"))
card_word        = canvas.create_text(400, 263, text = '', font = ("Arial", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR)
canvas.grid(row  = 0,column = 0,columnspan = 2,padx = (50,50))

## -------------------------- Button ----------------------------------------- #

unknown_button = Button(image = wrong,highlightthickness = 0, command = next_word)
unknown_button.grid(row = 1,column = 0)
right_button = Button(image = right,highlightthickness = 0, command = next_word)
right_button.grid(row = 1,column = 1)

next_word()
window.mainloop()