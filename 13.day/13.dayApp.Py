print("Exam Grade Calculator")
print()
nameOfExam = input("Name of exam: ")
print()
maxScore = int(input("Enter the maximum possible score: "))
print()
yourScore = int(input("Enter your score: "))
print()
percentage = (yourScore / maxScore) * 100
percentage = round(percentage, 2)
if percentage >= 90:
  print(percentage, " => A")
elif percentage >= 80:
  print(percentage, " => B")
elif percentage >= 70:
  print(percentage, " => C")
elif percentage >= 60:
  print(percentage, " => D")
else:
  print(percentage, " => F")
