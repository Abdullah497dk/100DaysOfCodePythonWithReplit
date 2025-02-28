print("Replit Login System")
print()

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "Abdullah" and password == "Abdullah123":
            print("Welcome back Abdullah!")
            break
        else:
            print("Invalid username or password!")
            print("Try again.")
            continue

login()
print()