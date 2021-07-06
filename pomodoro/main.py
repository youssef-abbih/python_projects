from tkinter import Tk, Canvas, PhotoImage, Label, Button
from PIL import ImageTk, Image
from math import floor
# ---------------------------- CONSTANTS --------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass
# ---------------------------- TIMER MECHANISM --------------------------- # 
def start_timer():
    count_down(300)

# ---------------------------- COUNTDOWN MECHANISM ----------------------- # 
def count_down(count):
    count_minut = floor(count / 60)
    count_second = count % 60
    if count_minut < 10:
        count_minut = f'0{count_minut}'
    if count_second < 10:
        count_second = f'0{count_second}'
    canvas.itemconfig(timer_text,text = f'{count_minut}:{count_second}')
    if count >0:
        window.after(1000,count_down,count-1)


# ---------------------------- UI SETUP ---------------------------------- #

## ---------------------------- Window ----------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx = 100, pady = 50,bg = YELLOW)

## --------------------------- Label ------------------------------------- #

label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME,35))
label.grid(row = 0,column = 1)
check_mark = Label(text = "✓", bg = YELLOW, fg = GREEN, font = (FONT_NAME,35))
check_mark.grid(row = 2, column = 1)
## --------------------------- Image ------------------------------------- #

img = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas = Canvas(width = 200, height = 224, bg = YELLOW,highlightthickness = 0)
canvas.create_image(100,112,image = img)
timer_text = canvas.create_text(100,130,fill = "white",font = (FONT_NAME ,35,'bold'),text = "00:00")
canvas.grid(row = 1,column = 1)

## -------------------------- Button ------------------------------------- #

start = Button(text = 'Start', bg = YELLOW, highlightthickness = 0, command = start_timer)
start.grid(row = 2, column = 0)
reset = Button(text = 'Reset', bg = YELLOW, highlightthickness = 0,command = reset_timer)
reset.grid(row = 2, column = 2)

window.mainloop()

