import random

def hi_lo(num, win_num):
    if num == win_num:
        return False
    if num > win_num:
        return 'high'
    if num < win_num:
        return 'low'

win_number = random.randint(1,100)
guesses = 0

while True:
    current_guess = int(input("enter a number: "))
    guesses+=1
    result = hi_lo(current_guess,win_number)
    if result == False:
        break
    print (f'Your guess was too {result}. Try again!')

print(f'You won! it took you {guesses} guesses')

