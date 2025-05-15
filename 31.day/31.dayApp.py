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


colorfulPrint("=", "red")
colorfulPrint("=", "white")
colorfulPrint("=", "blue")
colorfulPrint(" Music App ", "yellow")
colorfulPrint("=", "blue")
colorfulPrint("=", "white")
colorfulPrint("=", "red")

print("\n")
Rg = "radio gaga"
q = "queen"
print(f"🎵 {Rg: >13}")
print(f"{q: >12}")
print("\n")
print()
print("Prev")
next = colorfulPrint("Next", "cyan")

print(f""\033[36m" {next: >6}")
print("")