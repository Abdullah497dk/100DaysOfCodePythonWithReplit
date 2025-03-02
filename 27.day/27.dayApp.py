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



os.system('cls')
print("Welcome to the Character Builder App")
print()

while True:
    pygame.init()
    pygame.mixer.music.load("27.day/tokyo_ghoul_ac.mp3")
    pygame.mixer.music.play(-1)
    print("Enter your character's name:")
    name = input()
    print("Enter Character's type(Human, Elf, Wizerd, Ork): ")
    type = input()
    strong = 0
    health = 0
    strong = (diceRoll6() * diceRoll8())/2 + 12
    health = (diceRoll6() * diceRoll12())/2 + 10
    print()
    print("Creating character...")
    time.sleep(2)
    print("Your character's name is: " + name) 
    time.sleep(2.5)
    print("Your character's type is: " + type)
    time.sleep(2.5)
    print("Your character's strong is: " + str(strong))
    time.sleep(2.5)
    print("Your character's health is: " + str(health))
    time.sleep(4)
    print()
    print("Do you want to create another character? (yes or no)")
    answer = input()
    if answer == "no":
        break
    elif answer == "yes":
        print("Creating another character...")
        time.sleep(2)
        os.system('cls')
        continue
    else:
        print("Invalid input")
        break

os.system('cls')
time.sleep(1)
print("Goodbye!..")
