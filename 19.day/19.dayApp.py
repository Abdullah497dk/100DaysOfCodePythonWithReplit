print("laon calculater")
print()

money = int(input("Enter the amount of money you have >> "))
print()



for i in range(10) :   
    money = money * 1.05
    money = round(money, 2)
    print(i+1 , ". year: ", money)

count = round(money - 1000, 2)
print()
print("Total amount of money after 10 years: ", count)