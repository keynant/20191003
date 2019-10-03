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

        fm1 = Frame(self.root)
        self.title_label = Label(fm1, text = 'Guess a number: ', font = ('david', 24))
        self.title_label.pack(side = 'top')
        self.guesses_label = Label(fm1, text='Guesses taken: '+str(self.guesses.get()), font=('david', 12))
        self.guesses_label.pack(side = 'top')

        # ----------
        # Entry area
        # ----------
        self.entry_label = Label(fm1, text='Guess a number: ', font=('david', 12))
        self.entry_label.pack(side = 'left')
        self.entry_val = IntVar()
        self.entry_box = Entry(fm1, font=('david', 12), textvariable=self.entry_val)
        self.entry_box.pack(side = 'left')
        # ----------
        # End entry area
        # ----------

        fm1.pack()

        # --------------------
        # result frame. should be visible only after one guess optimally.
        # --------------------
        fm2 = Frame(self.root)
        self.result_var = StringVar()
        self.result_var.set('Low')
        self.color_var = StringVar()
        self.color_var.set('Red')
        self.result_label = Label(fm2, text='Your guess was too '+self.result_var.get(), font=('david', 12),
                                  fg = self.color_var.get())
        self.result_label.pack(side = 'top')
        fm2.pack()
        # --------------------
        # end of result frame.
        # --------------------

        fm3 = Frame(self.root)
        self.guess_btn = Button(fm3, text = 'Guess', font=('david', 12)).pack(side = 'top', fill = X)
        self.new_game_btn = Button(fm3, text = 'New Game / Reset', font=('david', 12)).pack(side = 'left')
        self.exit_btn = Button(fm3, text = 'Exit', font=('david', 12), command=self.root.quit).pack(side = 'left')

        fm3.pack()

    def check_entry(self):
        if int(self.entry_box.get()) > self.winning_number.get(): #why is winning_number an IntVar?
            print('high')
        if int(self.entry_box.get()) < self.winning_number.get(): #why is winning_number an IntVar?
            print('low')
        if int(self.entry_box.get()) == self.winning_number.get(): #why is winning_number an IntVar?
            print('equal')
'''
def hi_lo(num, win_num):
    if num == win_num:
        return False
    if num > win_num:
        return 'high'
    if num < win_num:
        return 'low'
'''
root = Tk()
# root.geometry("500x500")
game_window = GameWindow(root)
game_window.entry_box.focus()
game_window.entry_box.bind('<Return>', (lambda event: game_window.check_entry()))
win_number = random.randint(1,100)
game_window.guesses.set(0)
root.mainloop()



'''
while True:
    current_guess = int(input("enter a number: "))
    game_window.guesses.set(game_window.guesses.get()+1)
    result = hi_lo(current_guess,win_number)
    if result == False:
        break
    print (f'Your guess was too {result}. Try again!')

print(f'You won! it took you {guesses} guesses')
'''
