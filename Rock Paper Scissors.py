# Rock Paper Scissors
# Written by Sam
# 18/03/25


# Libraries:
import random

# Player Stats
playerStr = random.randint(1,100)
playerDex = random.randint(1,100)
playerInt = random.randint(1,100)
playerHP = random.randint(1,50) + 50

# Functions:
def theSystem():
    print('Rock, Paper or Scissors?')
    pInp = input('> ')
    random_result = random.randint(1,3) # The RNG
    # Draws
    if pInp == 'Rock' and random_result == 1:
        print('Enemy chose Rock')
        print('It\'s a draw!')
           
    if pInp == 'Paper' and random_result == 2:
        print('Enemy chose Paper')
        print('It\'s a draw!')
           
    if pInp == 'Scissors' and random_result == 3:
        print('Enemy chose Scissors')
        print('It\'s a draw!')
           
    # Enemy victory
    if pInp == 'Rock' and random_result == 2:
        print('Enemy chose Paper')
        print('Enemy wins!')
           
    if pInp == 'Paper' and random_result == 3:
        print('Enemy chose Scissors')
        print('Enemy wins!')
           
    if pInp == 'Scissors' and random_result == 1:
        print('Enemy chose Rock')
        print('Enemy wins!')
           
    # Player Victory
    if pInp == 'Rock' and random_result == 3:
        print('Enemy chose Scissors')
        print('Player wins!')
           
    if pInp == 'Paper' and random_result == 1:
        print('Enemy chose Rock')
        print('Player wins!')
           
    if pInp == 'Scissors' and random_result == 2:
        print('Enemy chose Paper')
        print('Player wins!')

def retPlayername():
    print('Your name is:',playerName)
def retPlayerstats():
    print('Your Strength is: ',playerStr)
    movLine()
    print('Your Dexterity is: ',playerDex)
    movLine()
    print('Your Intelligence is: ',playerInt)
def retPlayerhealth():
        print('Your max HP is: ',playerHP)

def movLine():
    movLine1 = input('')

# Main Code:

print('Welcome to Way of the Rock, a Rock Paper Scissors RPG game!')
movLine()
print('To enter the dungeon, you first need to create a character!')
movLine()
print('First, enter your character\'s name.')
playerName = input('> ')
print('Secondly, I will calculate your character\'s stats: ')
retPlayerstats()
movLine()
print('Now we will calculate your character\'s health.')
retPlayerhealth()
movLine()
print('With your character created, you can enter the dungeon!')

# Rooms

rooms = [room1]

def room1():
    print('The walls are dank and the room smells of rotting corpses.')
    print('The room is empty.')


roomThing