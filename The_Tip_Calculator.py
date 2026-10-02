print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage (5,10,12,15..) tip would you like to give? "))
people = int(input("How many people to split the bill? "))
pay = round((bill / people) * (1 + tip / 100), 2)
print(f"Each person should pay : ${pay} ")
fff
