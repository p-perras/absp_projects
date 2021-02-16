#! python3
# coinToss.py
# ABSP - Chapter 11

import random

guess = ''
options = ['tails', 'heads']

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

if options[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if options[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
