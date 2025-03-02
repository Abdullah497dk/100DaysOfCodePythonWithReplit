from getpass import getpass as input
print("Epic Rock Paper Scissors Game")
print()
print("Enter R for Rock, P for Paper, S for Scissors")
print()
playerOne = input("Player 1 >> ")
playerTwo = input("Player 2 >> ")
print()
if playerOne == playerTwo:
  print("It's a tie!")
elif playerOne == "R":
    if playerTwo == "P":
        print("Player 2 wins!")
        print("Paper(2.) covers Rock(1.)")
    else:
        print("Player 1 wins!")
        print("Rock(1.) crushes Scissors(2.)")
elif playerOne == "P":
    if playerTwo == "S":
        print("Player 2 wins!")
        print("Scissors(2.) cuts Paper(1.)")
    else:
        print("Player 1 wins!")
        print("Paper(1.) covers Rock(2.)")
elif playerOne == "S":
    if playerTwo == "R":
        print("Player 2 wins!")
        print("Rock(2.) crushes Scissors(1.)")
    else:
        print("Player 1 wins!")
        print("Scissors(1.) cuts Paper(2.)")

