print("Fake Fan Finder")
print("---------------")
anime = input("What's your favourite Anime? ")
if anime == "Naruto":
  print(anime, "is a great anime!")
  favCharacter = input("Who's your favourite character? ")
  if favCharacter == "Naruto":
    print("Naruto is the best!")
  elif favCharacter == "Sasuke":
    print("hmm.. Sasuke is the good too!")
  else:
    print("Are you kidding with me!")
  stronger = input("Who's stronger?Naruto or Sasuke?(in the end of the anime) ")
  if stronger == "Naruto":
    print("You are a true fan!")
  else:
    print("You are a fake fan of " + anime + "!")
elif anime == "Death Note":
  print("Death Note is a great anime!")
  favCharacter = input("Who's your favourite character? ")
  if favCharacter == "Light":
    print("Light was very good character but he die!")
  elif favCharacter == "Kira":
    print("Kira is the best!")
  else:
    print("Are you kidding with me!")
  winner = input("Who winnig at the end of the anime?Kira or Light? ")
  if winner == "Kira":
    print("You are a true fan!")
  else:
    print("You are a fake fan of " + anime + "!")
elif anime == "Tokyo Ghoul":
  print("Tokyo Ghoul is a great anime!")
  favCharacter = input("Who's your favourite character? ")
  if favCharacter == "Kaneki":
    print("Ken Kaneki is the best!")
  elif favCharacter == "Touk":
    print("Touka Kirishima is the good too!")
  else:
    print("Are you kidding with me!")
  winner = input("Who stronger ghoul at the end of the anime?  ")
  if winner == "Kaneki":
    print("You are a true fan!")
  else:
    print("You are a fake fan of " + anime + "!")

else:
  print("I don't know this anime!")
  print("You are a fake fan of anime world!")
    