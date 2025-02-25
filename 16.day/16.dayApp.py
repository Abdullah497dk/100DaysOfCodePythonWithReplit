print("Fill the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")
print("if you can't guess, type 'exit' to leave.")
print()
count = 0
while True:
  print("Never going to ______ up again.")
  word = input("What is the missing word? ")
  count = count + 1
  if word == "give":
    print("You are correct!")
    print("You got it in", count, "tries.")
    break
  elif word == "exit":
    print("Goodbye!")
    break
