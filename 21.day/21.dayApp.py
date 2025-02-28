print("Math Game")
print()
mainNumber = int(input("Enter the number you want to play with >> "))
print()

count = 0

for i in range(1, 11):
    print(mainNumber, "x", i, "= ")
    answer = int(input())
    if answer == mainNumber * i:
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")
        print("The correct answer is", mainNumber * i)
        continue
print()

print("You got", count, "correct answers.")
print()