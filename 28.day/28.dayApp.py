import random
import time
import os
import pygame

def diceRoll6():
    return random.randint(1, 6)
def diceRoll8():
    return random.randint(1, 8)
def diceRoll12():
    return random.randint(1, 12)
def diceRoll3():
    return random.randint(1, 3)


os.system('cls')
print("Welcome to the Character Builder App")
print()

while True:
    pygame.init()
    pygame.mixer.music.load("27.day/tokyo_ghoul_ac.mp3")
    pygame.mixer.music.play(-1)
    print("Enter your character's name:")
    player1name = input()
    print("Enter Character's type(Human, Elf, Wizerd, Ork): ")
    player1type = input()
    player1strong = 0
    player1health = 0
    player1strong = (diceRoll6() * diceRoll8())/2 + 12
    player1health = (diceRoll6() * diceRoll12())/2 + 10
    print()
    print("Creating character...")
    time.sleep(2)
    print("Your character's name is: " + player1name) 
    time.sleep(2.5)
    print("Your character's type is: " + player1type)
    time.sleep(2.5)
    print("Your character's strong is: " + str(player1strong))
    time.sleep(2.5)
    print("Your character's health is: " + str(player1health))
    time.sleep(4)
    print()

    print("Who are they fighting against?")
    print("Enter your 2. character's name:")
    player2name = input()
    print("Enter Character's type(Human, Elf, Wizerd, Ork): ")
    player2type = input()
    player2strong = 0
    player2health = 0
    player2strong = (diceRoll6() * diceRoll8())/2 + 12
    player2health = (diceRoll6() * diceRoll12())/2 + 10
    print()
    print("Creating character...")
    time.sleep(2)
    print("Your character's name is: " + player2name)  
    time.sleep(2.5)
    print("Your character's type is: " + player2type)
    time.sleep(2.5)
    print("Your character's strong is: " + str(player2strong))
    time.sleep(2.5)
    print("Your character's health is: " + str(player2health))
    time.sleep(4)
    print()
    print("Press Enter to start the fight")
    startfight = input()
    print("Loading...")
    time.sleep(2)
    os.system('cls')
    print("Fighting...")
    time.sleep(2)
    os.system('cls')
    print()
    print(player1name + " vs " + player2name)
    count = 1
    while True:
        print("Round " + str(count))
        time.sleep(2)
        attack1 = diceRoll3()*player1strong/25
        attack2 = diceRoll3()*player2strong/25
        player2health = player2health - attack1
        player1health = player1health - attack2
        print(player1name + " attacks " + player2name + " with " + str(attack1) + " damage")
        time.sleep(2)
        print(player2name + " attacks " + player1name + " with " + str(attack2) + " damage")
        time.sleep(2)
        print(player1name + " health: " + str(player1health))
        time.sleep(2)
        print(player2name + " health: " + str(player2health))
        time.sleep(5)
        count += 1
        if player1health <= 0:
            print(player2name + " wins!")
            break
            quit()
        elif player2health <= 0:
            print(player1name + " wins!")
            break
            quit()
        print()
        os.system('cls')
    