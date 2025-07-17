import tkinter
from tkinter import *
from textblob import TextBlob

window = Tk()
window.title("Spelling Check")
window.geometry("700x400")
window.config(background="white")

def check_spelling():
    word = enter_text.get()
    blob = TextBlob(word)
    corrected_text = str(blob.correct())

    cs = Label(window, text="Corrected Text:", font=("Times", 20), bg="white", fg="#364971")
    cs.place(x=100, y=250)
    spell.config(text=corrected_text)

heading = Label(window, text="Spelling Check", font=("Times", 30, "bold"), bg="white", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(window, justify="center", width=30, font=("Times", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(window, text="Check", font=("Times", 30, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

spell = Label(window, font=("Times", 25), bg="white", fg="#364971")
spell.place(x=350, y=250)

window.mainloop()
