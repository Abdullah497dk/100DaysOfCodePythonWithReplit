print("30 Days Down - What did you think?")
print()
count = 1
while True:
    print(f"What did you think of {count}.day")
    input_text = input("Enter your thoughts: ")
    print()
    myText = f"Day {count} you thought"
    print(f"{myText: ^50}")
    print(f"{input_text: ^50}")
    print()
    count += 1
    if count > 30:
        break