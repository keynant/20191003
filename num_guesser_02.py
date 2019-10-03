import random
from tkinter import *
import time

class GameWindow:
    def __init__(self,root):
        self.root = root
        self.root.title('Number Guesser')
        self.winning_number = IntVar()
        self.winning_number.set(random.randint(0,100))
        self.guesses = IntVar()
        self.guesses.set(0)

        self.title_label = Label(root, text = 'Guess a number: ', font = ('david', 24))
        self.title_label.pack()
        self.guesses_label = Label(root, text='Guesses taken: '+str(self.guesses.get()), font=('david', 12))
        self.guesses_label.pack()




def hi_lo(num, win_num):
    if num == win_num:
        return False
    if num > win_num:
        return 'high'
    if num < win_num:
        return 'low'

root = Tk()
root.geometry("500x500")
game_window = GameWindow(root)
root.mainloop()

win_number = random.randint(1,100)
game_window.guesses.set(0)

while True:
    current_guess = int(input("enter a number: "))
    game_window.guesses.set(game_window.guesses.get()+1)
    result = hi_lo(current_guess,win_number)
    if result == False:
        break
    print (f'Your guess was too {result}. Try again!')

print(f'You won! it took you {guesses} guesses')

