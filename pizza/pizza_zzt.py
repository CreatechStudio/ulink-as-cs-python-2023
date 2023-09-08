print("Welcome to Ulink Pizza Club!")

# Define costs
sizes = {'S': 150, 'M': 200, 'L': 250}
pepperoni_costs = {'S': 20, 'M': 30, 'L': 30}
chocolate_costs = {'S': 40, 'M': 50, 'L': 60}
extra_cheese_cost = 10

# Get user input
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
add_chocolate = input("Do you want chocolate? Y or N ")

# Compute bill
bill = sizes.get(size.upper(), 0)  # Pizza cost
bill += pepperoni_costs.get(size.upper(), 0) if add_pepperoni.upper() == 'Y' else 0  # Pepperoni cost
bill += chocolate_costs.get(size.upper(), 0) if add_chocolate.upper() == 'Y' else 0  # Chocolate cost
bill += extra_cheese_cost if extra_cheese.upper() == 'Y' else 0  # Extra cheese cost

print(f"Your final bill is: ${bill}.")