import os
import time

print("MyPod Music Player")
print()
print("Press 1 to Play")
print("Press 2 to Exit")
print("Press anything else to see the menu again")
while True:
  user_input = input()
  if user_input == "1":
    print("Playing some proper tunes!")
    time.sleep(2)
    os.system("clear")
    continue
  elif user_input == "2":
    print("Exiting the program")
    time.sleep(2)
    os.system("clear")
    break
  else:
    time.sleep(1)
    os.system("clear")
    