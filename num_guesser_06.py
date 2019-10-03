import random
from tkinter import *
import time
import os
import json


class GameWindow:
    def __init__(self, root):
        self.start_time = (time.strptime(time.ctime())[4],time.strptime(time.ctime())[5])
        self.root = root

        self.root.title('Number Guesser')
        self.guesses = IntVar()
        self.winning_number = random.randint(0, 100)
        self.guesses.set(0)

        title_fm = Frame(self.root)
        self.title_label = Label(title_fm, text='Guess a number: ', font=('david', 24))
        self.title_label.pack(side='top')
        title_fm.pack()

        # ----------
        # Entry area
        # ----------
        entry_fm = Frame(self.root)
        self.entry_label = Label(entry_fm, text='Guess a number: ', font=('david', 12))
        self.entry_label.pack(side='left')
        self.entry_box = Entry(entry_fm, font=('david', 12))
        self.entry_box.pack(side='left')
        entry_fm.pack()
        # ----------
        # End entry area
        # ----------

        # --------------------
        # result frame. should be visible only after one guess optimally.
        # --------------------
        result_fm = Frame(self.root)
        self.result_var = StringVar()
        self.result_var.set('Please enter a guess')
        self.result_label = Label(result_fm, textvariable=self.result_var, font=('david', 12),
                                  fg='Black')
        self.result_label.pack()
        result_fm.pack()
        # --------------------
        # end of result frame.
        # --------------------

        guesses_fm = Frame(self.root)
        self.guesses_label = Label(guesses_fm, text='Guesses taken: ', font=('david', 12)).pack(side='left')
        self.guesses_var_label = Label(guesses_fm, textvariable=str(self.guesses), font=('david', 12)).pack(side='left')
        guesses_fm.pack()

        time_fm = Frame(self.root)
        self.time_var = StringVar()
        self.time_var.set("00:00")
        self.time_label = Label(time_fm, text = 'Elapsed time: ', font=('david', 12)).pack(side='left')
        self.time_var_label = Label(time_fm, textvariable = self.time_var, font=('david', 12)).pack(side='left')
        time_fm.pack()


        buttons_fm = Frame(self.root)
        self.guess_btn = Button(buttons_fm, text='Guess', command=self.check_entry, font=('david', 12))
        self.guess_btn.pack(side='top', fill=X)
        self.new_game_btn = Button(buttons_fm, text='New Game / Reset', command=self.check_new_game, font=('david', 12)).pack(
            side='left')
        self.exit_btn = Button(buttons_fm, text='Exit', font=('david', 12), command=self.root.quit).pack(side='left')

        buttons_fm.pack()

    def check_new_game(self):
        self.newgame_fm = Frame(self.root)
        self.sure_lbl = Label(self.newgame_fm, text='are you sure?', font=('david', 12)).pack()
        self.yes_btn = Button(self.newgame_fm, text='Yes', command=self.new_game, font=('david', 12))
        self.yes_btn.pack(side='left', fill=X)
        self.no_btn = Button(self.newgame_fm, text='No', command = self.newgame_fm.destroy, font=('david', 12)).pack(side='left')
        self.newgame_fm.pack()

    def new_game(self):
        self.start_time = time.time()
        self.time_var.set('00:00')
        self.newgame_fm.destroy()
        self.winning_number = random.randint(0, 100)
        self.guesses.set(0)
        self.result_var.set('Please enter a guess')
        self.result_label.config(fg='black')
        self.guess_btn.config(state='normal')

    def check_entry(self):
        self.update_time()
        if 'disabled' in self.guess_btn.config()['state']:
            self.entry_box.delete('0', END)
            return
        if self.entry_box.get() == '':
            return
        if not self.entry_box.get().isdecimal():
            self.result_label.config(fg='black')
            self.result_var.set(f'{self.entry_box.get()} is not a valid number')
            return
        elif int(self.entry_box.get()) > self.winning_number:
            print('high')
            self.result_var.set(f'{self.entry_box.get()} is too high')
            self.result_label.config(fg='red')

        elif int(self.entry_box.get()) < self.winning_number:
            print('low')
            self.result_var.set(f'{self.entry_box.get()} is too low')
            self.result_label.config(fg='blue')

        elif int(self.entry_box.get()) == self.winning_number:
            self.result_var.set(f'{self.entry_box.get()} is correct!')
            self.result_label.config(fg='green')
            self.guess_btn.config(state=DISABLED)
        self.guesses.set(self.guesses.get() + 1)
        self.entry_box.delete('0', END)

    def update_time(self):
        current_time = (time.strptime(time.ctime())[4], time.strptime(time.ctime())[5])
        elapsed_time = (current_time[0] - self.start_time[0], current_time[1] - self.start_time[1])
        if elapsed_time[1] <= 9 and elapsed_time[0] <= 9:
            self.time_var.set(f'0{elapsed_time[0]}:0{elapsed_time[1]}')
        if elapsed_time[0] <= 9 and elapsed_time[1] > 9:
            self.time_var.set(f'0{elapsed_time[0]}:{elapsed_time[1]}')
        if elapsed_time[0] > 9 and elapsed_time[1] > 9:
            self.time_var.set(f'{elapsed_time[0]}:{elapsed_time[1]}')
        if elapsed_time[0] > 9 and elapsed_time[1] <= 9:
            self.time_var.set(f'{elapsed_time[0]}:0{elapsed_time[1]}')

    def score_board(self):
        pass

    def enter_name(self):
        pass


def mk_hiscore_dir():
    os.chdir('c:/')
    print(os.getcwd())
    success = True
    try:
        os.mkdir('NumGuesser')
    except WindowsError as e:
        if e.winerror == 183:
            print("Directory exists")
        else:
            print(e)
    try:
        os.chdir('NumGuesser')
    except Exception as e:
        print(e)
        success = False
    return success


def search_add_name_hiscore(name,d):
    if name in d.keys():
        print("name found")
    else:
        with open("c:/NumGuesser/HiScore_list.txt", 'w') as f1:
            print("name added")
            d[name] = 0
            json.dump(d, f1)


def create_hiscore_list():
    if "HiScore_list.txt" in os.listdir(os.getcwd()):
        with open("c:/NumGuesser/HiScore_list.txt",'r') as f1:
            print('list exists')
            return json.load(f1)
    else:
        with open("c:/NumGuesser/HiScore_list.txt", 'w+') as f1:
            f1.write('{}')
            f1.seek(0)
            print('list created')
            return json.load(f1)

mk_hiscore_dir()

name = 'key'
hiscore_list = create_hiscore_list()  #create/load list into dict
search_add_name_hiscore(name, hiscore_list)



root = Tk()
game_window = GameWindow(root)

game_window.entry_box.focus()
game_window.entry_box.bind('<Return>', (lambda event: game_window.check_entry()))

game_window.guesses.set(0)
root.mainloop()


# TODO: add name and HiScore implementation in Tk
