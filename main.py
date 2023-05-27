from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:  # Throws error the first time program is run.
    # So, we catch the exception
    data = pandas.read_csv('data/french_words.csv')
    words = data.to_dict(orient='records')
else:
    words = data.to_dict(orient='records')



def generate_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(title, text='French', fill='white')
    canvas.itemconfig(word, text=current_card['French'], fill='white')
    canvas.itemconfig(canvas_image, image=card_back)
    flip_timer = window.after(2000, func=flip_card)


def is_known_card():
    global words
    words.remove(current_card)
    generate_card()
    data = pandas.DataFrame(words)
    data.to_csv('data/words_to_learn.csv', index=False)  # index=False is added to remove additional index that gets
    # added each time the program runs


def flip_card():
    global current_card
    canvas.itemconfig(title, text='English', fill='black')
    canvas.itemconfig(word, text=current_card['English'], fill='black')
    canvas.itemconfig(canvas_image, image=card_front)


window = Tk()
window.title('Flash Card App - French')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(400, 263, image=card_back)
title = canvas.create_text(400, 150, font=('Arial', 40, 'italic'), fill='white')
word = canvas.create_text(400, 263, font=('Arial', 60, 'bold'), fill='white')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known_card)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=generate_card)
wrong_button.grid(row=1, column=0)

generate_card()

window.mainloop()
