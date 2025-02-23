print("Tips Calculator")
print()
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))
bill = (total * (1 + tip)) / people
print(f"Each person should pay: ${bill:.2f}")