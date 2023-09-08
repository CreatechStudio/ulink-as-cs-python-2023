def get_input(prompt, valid_options):
    """
    Prompt the user for input and validate against a set of valid options.

    :param prompt: A string containing the prompt to be displayed to the user.
    :param valid_options: A list of valid options that the user's response can match.
    :return: The user's response if it matches one of the valid options.
    """
    while True:
        response = input(prompt).upper()
        if response in valid_options:
            return response
        print("Invalid entry. Please try again.")

def calculate_price():
    """
    Calculate the price of a pizza order at Ulink Pizza Cafe.

    :return: None
    """
    print("Welcome to Ulink Pizza Cafe")

    size = get_input("What size pizza do you want? S, M, or L?", ['S', 'M', 'L'])
    add_pe = get_input("Do you want pepperoni? Y or N?", ['Y', 'N'])
    extra_c = get_input("Do you want extra cheese? Y or N?", ['Y', 'N'])
    # Input

    price = 0
    sizes = {'S': 150, 'M': 200, 'L': 250}
    pepperoni_prices = {'Y': 20, 'N': 0} if size == 'S' else {'Y': 30, 'N': 0}

    price += sizes.get(size, 0)
    price += pepperoni_prices.get(add_pe, 0)
    if extra_c == 'Y':
        price += 10

    print(f"Your final bill is {price}")

calculate_price()