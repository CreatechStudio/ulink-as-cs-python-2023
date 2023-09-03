print("Welcome to the tip calculator.")
bill_price = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = bill_price + (bill_price * tip_percentage / 100)
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")