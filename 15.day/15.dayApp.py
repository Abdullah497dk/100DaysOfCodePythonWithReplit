
exit = False
while not exit:
    animalName = input("What animal you want: ")
    if animalName == "dog":
        print("Woof Woof")
    elif animalName == "cat":
        print("Meow")
    elif animalName == "cow":
        print("Moo")
    elif animalName == "duck":
        print("Quack")
    elif animalName == "lion":
        print("Roar")
    elif animalName == "elephant":
        print("Trumpet")
    elif animalName == "turtle":
        print("grrrrr")
    else:
        print("I don't know that animal")
        print("Ask again if you want")
    

    print()
    exitInput = input("Do you want to exit?y/n: ")
    if exitInput == "y":
        exit = True
        print("Goodbye!")
    else:
        exit = False
        print()
        print("Let's play again!")
        print()
    


    