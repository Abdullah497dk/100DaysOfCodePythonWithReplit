print("List Generator")
print()

startPoint = int(input("Enter the starting point of the list >> "))
endPoint = int(input("Enter the ending point of the list >> "))
howItincrease = int(input("Enter the number of increase >> "))
print()

for i in range(startPoint, endPoint, howItincrease):
    print(i)
print()

exit()
