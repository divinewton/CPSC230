# In class activity, Week 4 Friday

MoneyInBank = True
UserMoney = int(input("How much money is in your account? "))
while MoneyInBank:
    if UserMoney > 0:
        UserMoney -= 1
        print("You have money!")
    else: MoneyInBank = False
print("You're poor now")