from tkinter import *


def convert_mile_to_kilometer():
    km = float(entry.get()) * 1.609
    text_3.config(text=round(km, 2))


window = Tk()
window.title('Mile to Kilometer conversion')
window.minsize(width=200, height=200)
window.config(padx=30, pady=30)

entry = Entry()
entry.grid(row=0, column=1)

text_1 = Label(text='miles')
text_1.grid(row=0, column=2)

text_2 = Label(text='is equal to')
text_2.grid(row=1, column=0)

text_3 = Label(text='0')
text_3.grid(row=1, column=1)

button = Button(text='Calculate', command=convert_mile_to_kilometer)
button.grid(row=2, column=1)

text_4 = Label(text='km')
text_4.grid(row=1, column=2)


window.mainloop()
