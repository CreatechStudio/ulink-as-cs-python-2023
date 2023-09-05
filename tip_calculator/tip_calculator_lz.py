bill = float(input("What was the total bill?")[1:])
per = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
peo = int(input("How many people to split the bill?"))
print(f"Each person should pay: ${round(bill/100*per/peo + bill/peo, 2)}")
# ashjkldghlaskdhgjlsa