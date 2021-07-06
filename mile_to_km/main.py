from tkinter import *

window = Tk()
window.title = ('Mile to KM converter')

input = Entry()
input.grid(column = 1, row = 0)

miles = Label(text = 'Miles')
miles.grid(column = 2, row = 0)

equal = Label(text = 'is equal to')
equal.grid(column = 0 , row = 1)

result = Label(text = 0)
result.grid(column = 1, row = 1)

km = Label(text = 'KM')
km.grid(column = 2, row = 1)


def calculate():
    miles = float(input.get())
    km = miles*1.609
    result['text'] = km
button = Button(text = 'Calculate',command = calculate)
button.grid(column = 1, row = 2)

window.mainloop()
