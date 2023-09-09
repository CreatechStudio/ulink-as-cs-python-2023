# Tip calculator Python

total_bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
people_num = int(input("How many people to split the bill? "))

tip_to_pay = round((total_bill / people_num) * percentage_tip, 6)
money_to_pay = round(tip_to_pay + total_bill/people_num, 2)

print(f"Each person should pay: ${money_to_pay}")
