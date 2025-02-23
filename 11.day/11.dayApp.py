print("How Many Seconds Are In A Year?")
print()
leapYear = input("Is it a leap year?y/n: ")

sec = 1
min = sec * 60
hour = min * 60
day = hour * 24
month = day * 30
year = month * 12

if leapYear == "y":
  print(year + day)
else:
  print(year)
