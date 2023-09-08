def pizza():

    print("Welcome to Ulink Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")

    cost = 0

    if size not in ['S', 'M', 'L']: return True
    if size == 'S': cost += 150
    elif size == 'M': cost += 200
    else: cost += 250
            
    
    if add_pepperoni not in ['Y', 'N']: return True
    if add_pepperoni == 'Y':
        if size == 'S': cost += 20
        else: cost += 30

    if extra_cheese not in ['Y', 'N']: return True
    if extra_cheese == 'Y': cost += 10


    print(f"The total cost of the pizza is ${cost}")
    return False

    
while pizza():
    print("Your input is invalid, Please try again \n")