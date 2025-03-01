print("Infinity Dice")
print()


def rollDice(slides):
  import random
  while True:
    roll = random.randint(1,slides)
    print("You rolled", roll)
    print()
    again = input("Roll again?: ")
    if again == "yes":
      continue
    else:
      break


slides = int(input("How many slides?: "))
rollDice(slides)

print("Thanks for playing! 😊")

