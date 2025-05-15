def colorfulPrint (text, color):
    if color == "red":
        print("\033[31m", text, sep="", end="")
    elif color == "green":
        print("\033[32m", text, sep="", end="")
    elif color == "yellow":
        print("\033[33m", text, sep="", end="")
    elif color == "blue":
        print("\033[34m", text, sep="", end="")
    elif color == "purple":
        print("\033[35m", text, sep="", end="")
    elif color == "cyan":
        print("\033[36m", text, sep="", end="")
    elif color == "white":
        print("\033[37m", text, sep="", end="")
    else:
        print("\033[0m", text, sep="", end="")

print("Super subrotine")
print()
print( "With my", end=" ")
colorfulPrint("new program ", "purple")
colorfulPrint( "I can just call ", "reset")
colorfulPrint("red('and') ", "red")
colorfulPrint( "and that word will appear in the color I set it to.", "reset")
print()
colorfulPrint("With no weird gaps.", "cyan")
print()
colorfulPrint("Epic", "reset")