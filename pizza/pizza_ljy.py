# initialize
size = None
price = 0

# welcome page
print("Welcome to Python Pizza Deliveries!")

# handle size including error check
size = input("What size pizza do you want? S, M, or L ").strip().upper()
while size not in ("S", "M", "L"):
    print("Not a choice")
    size = input("What size pizza do you want? S, M, or L ").strip().upper()
match size:
    case "S":
        price = 150
    case "M":
        price = 200
    case "L":
        price = 250

# handle pepperoni with error check
pepperoni = input("Do you want pepperoni? Y or N ").strip().upper()
while pepperoni not in ("Y", "N"):
    print("Not a choice")
    pepperoni = input("Do you want pepperoni? Y or N ").strip().upper()
if pepperoni == "Y":
    if size == "S":
        price += 20
    else:
        price += 30


# handle cheese with error check
cheese = input("Do you want extra cheese? Y or N ").strip().upper()
while cheese not in ("Y", "N"):
    print("Not a choice")
    cheese = input("Do you want extra cheese? Y or N ").strip().upper()
if cheese == "Y":
    price += 10
print(f"You final bill is: ${price}.")
