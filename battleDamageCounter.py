#!/usr/bin/env python3
# Name: battleDamageCounter.py
# Author: Mark Garcia
# Date: 10/16/2019

import random

# Define Player 1 Counter Function
def p1Counter(p1Life, hit):
    total = p1Life - hit
    return total

def life_Check(player1Life):
    if player1Life > 0:
        print('Player 1 is still alive!')
    else:
        print('Player 1 has died!')
    return()

# Initialize Player 1's starting life total
p1_Starting_Life = 20

# First Hit
hit = random.randrange(1, 20) #Pick 1 number between 1 and 20

# Calculate Player 1's Life Total
player1Life = p1Counter(p1_Starting_Life, hit)

# Output
print(f'\nPlayer 1 starting life is {p1_Starting_Life}')
print(f'Player 1 takes {hit} damage!')
print(f'Player 1 is now at {player1Life} health')

# Check if Player 1 is still alive
alive = life_Check(player1Life)

# Second Hit
hit = random.randrange(1, 20) #Pick 1 number between 1 and 20

# Calculate Player 1's Life Total
player1Life = p1Counter(player1Life, hit)

# Output
print(f'\nPlayer 1 takes {hit} damage!')
print(f'Player 1 is now at {player1Life} health')

# Check if Player 1 is still alive
alive = life_Check(player1Life)

# Third Hit
hit = random.randrange(1, 20) #Pick 1 number between 1 and 20

# Calculate Player 1's Life Total
player1Life = p1Counter(player1Life, hit)

# Output
print(f'\nPlayer 1 takes {hit} damage!')
print(f'Player 1 is now at {player1Life} health')

# Check if Player 1 is still alive
alive = life_Check(player1Life)
