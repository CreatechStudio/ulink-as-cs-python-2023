print('Welcome to the tip calculator')

total_bill = float(input('What is the total bill? $').strip())

tip = int(input('What percentage tip would you like to give? [10/12/15] ').strip())

while tip not in {10, 12, 15}:
	print('Your should only input 10, 12, or 15')
	tip = int(input('What percentage tip would you like to give? [10/12/15] ').strip())

tip_percent = (tip + 100) / 100

people_number = int(input('How many people to split the bill? ').strip())

print('Each person should pay: $' + str(round(total_bill * tip_percent / people_number, 2)))

