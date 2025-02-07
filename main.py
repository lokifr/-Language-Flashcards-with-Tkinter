from tkinter import *
import pandas as pd
import random
import os

# if words_to_learn.csv exists
if os.path.exists("words_to_learn.csv"):
    data = pd.read_csv("words_to_learn.csv")
else:
    data = pd.read_csv("./data/french_words.csv")

to_learn = data.to_dict(orient="records")

current_card = {}

def new_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(word, text=current_card['French'])
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(card_image, image=front_image)
    window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_card['English'])

def is_known():
    global to_learn
    to_learn.remove(current_card)
    data_to_save = pd.DataFrame(to_learn)
    data_to_save.to_csv("words_to_learn.csv", index=False)
    new_card()

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

new_card()

window.mainloop()
