print("Character stat generator")
print()


def rollDice6():
  import random
  dice6 = random.randint(1, 6)
  return dice6


def rollDice8():
  import random
  dice8 = random.randint(1, 8)
  return dice8


while True:
  input("Name your warrior: ")
  health = rollDice6() * rollDice8()
  print("Their health is: ", health, "hp")
  print()
  again = input("Want to create another character? ")
  if again == "yes":
    continue
  else:
    break

print("Thanks for playing!")