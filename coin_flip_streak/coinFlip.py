#! python3
# coinFlip.py
# ABSP - Chapter 4

import random

if __name__ == '__main__':

    numberOfStreaks = 0

    for experimentNumber in range(10000):
        
        coinFlip = []  
        for i in range(1, 101):
            coinFlip.append(random.randint(0, 1))
        # Code that checks if there is a streak of 6 heads or 6 tails in a row.
        streak = 1  # Any flip is a streak of (at least) 1; reset for next check
        for i in range(1, len(coinFlip)):  # Start at the second flip, as we will look back 1
            if coinFlip[i] == coinFlip[i-1]:  # Checks if current list item is the same as before
                streak += 1
            else:
                streak = 1
            if streak == 6:
                numberOfStreaks += 1
                break  # We've found a streak in this CoinFlip list, skip to next experiment

    print(f'There is a {numberOfStreaks / 100} chance of a streak of 6 in a 100 flips based on 10,000 rounds.')
