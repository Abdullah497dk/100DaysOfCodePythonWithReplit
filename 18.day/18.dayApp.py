import random

print("One-Thousand-To-One")
print()
print("Guess a number between 1 and 1,000")
print("If you can't guess the number, you can't leave the game by writing 'exit'")
print()
correct_number = round(random.randint(1, 1000))
while True:
    guess = input("Guess the number >> ")
    digit = guess.isdigit()
    if digit == False:
        print("Invalid input!")
        continue
    if guess == "exit":
        print("The number was:", correct_number)
        break
    elif int(guess) == correct_number:
        print("You guessed the number!")
        break
    elif int(guess) > correct_number:
        print("The number is lower than", guess)
    elif int(guess) < correct_number:
        print("The number is higher than", guess)
    else:
        print("Invalid input!")
        continue