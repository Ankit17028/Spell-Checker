import tkinter
from textblob import TextBlob
from tkinter import *
import time

class SpellChecker:
    def __init__(self):
        self.dictionary = set()

    def load_dictionary(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                self.dictionary.add(line.strip())

    def correct_text(self, text):
        corrected_words = []
        words = text.split()
        for word in words:
            if word.lower() not in self.dictionary:
                corrected_word = TextBlob(word).correct()
                corrected_words.append(str(corrected_word))
            else:
                corrected_words.append(word)
        return ' '.join(corrected_words)

def Auto_correct():
    Output_text.delete(1.0, END)
    text = Input_text.get(1.0, END)
    
    start_time = time.time()  # Start measuring runtime
    corrected_text = spell_checker.correct_text(text)
    end_time = time.time()  # End measuring runtime

    elapsed_time = end_time - start_time
    word_count = len(text.split())
    response_time_per_1000_words = (elapsed_time / word_count) * 1000
    print(f"Response time per 1000 words: {response_time_per_1000_words:.2f} seconds")

    Output_text.insert(END, corrected_text)


root = Tk()
root.geometry('1200x520')
root.resizable(0, 0)
root.title("Project-- Spell Check")
root.config(bg='blue')

Label(root, text="Enter Text", font='arial 18 bold', bg='white smoke').place(x=250, y=90)
Input_text = Text(root, font='arial 13', bg='black', fg='white', height=11, wrap=WORD, padx=5, pady=5, width=60,
                  insertbackground='white')
Input_text.place(x=30, y=130)

Label(root, text="Output", font='arial 18 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 13', bg='black', fg='white', height=11, wrap=WORD, padx=5, pady=5, width=60,
                   insertbackground='white')
Output_text.place(x=600, y=130)

auto_correct_btn = Button(root, text='Auto Correct', bg='#f55c33', font='arial 18 bold', pady=5, command=Auto_correct)
auto_correct_btn.place(x=510, y=360)

spell_checker = SpellChecker()
spell_checker.load_dictionary("check.txt")


root.mainloop()

