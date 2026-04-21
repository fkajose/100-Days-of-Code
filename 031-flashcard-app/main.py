from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
cards_deck = {}

try:
    with open('words_to_learn.csv', 'r') as new_deck:
        data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/1000 most frequent spanish words - Sheet2.csv')
    cards_deck = original_data.to_dict(orient='records')
else:
    cards_deck = data.to_dict(orient='records')


# TODO 1: Create UI

window = Tk()
window.title('Flashy Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file='./images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card_canvas.create_image(400, 263, image=card_front)
title_text = card_canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word_text = card_canvas.create_text(400, 263, text='word', font=('Arial', 60, 'bold'))
card_canvas.grid(row=0, column=0, columnspan=2)


# TODO 2: Create new flash cards


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(cards_deck)
    card_canvas.itemconfig(title_text, text='Spanish', fill='black')
    card_canvas.itemconfig(word_text, text=current_card['Spanish'], fill='black')
    card_canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def card_known():
    cards_deck.remove(current_card)
    updated_dataframe = pandas.DataFrame(cards_deck)
    updated_dataframe.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    card_canvas.itemconfig(canvas_image, image=card_back)
    card_canvas.itemconfig(title_text, text='English', fill='white')
    card_canvas.itemconfig(word_text, text=current_card['English'], fill='white')


flip_timer = window.after(3000, flip_card)


# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=card_known, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
