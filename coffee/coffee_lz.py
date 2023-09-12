def prompt_input(prompt, validator):
    while True:
        response = input(prompt).strip()

        if validator(response):
            return response

        print("Invalid entry. Please try again.")


def get_input(prompt, valid_options):
    validator = lambda response: response.upper() in valid_options
    return prompt_input(prompt, validator).upper()


def get_integer_input(prompt):
    validator = lambda response: response.isdigit()
    return int(prompt_input(prompt, validator))


def get_price_and_apply_discount(price, discount):
    return price * discount


def calculate_price():
    print("Welcome to Ulink Cafe")

    size = get_input("What size coffee do you want? S, M, or L: ", ['S', 'M', 'L'])
    milk = get_input("What type of milk do you want to add? R, A, O: ", ['R', 'A', 'O'])
    extra_s = get_input("Do you want an extra shot? Y or N: ", ['Y', 'N'])
    sugar = get_integer_input("How many sugar cubes would you like? ")

    sizes = {'S': 100, 'M': 150, 'L': 200}
    milk_types = {'R': 0, 'A': 20, 'O': 25}
    extra_shot_price = 30 if extra_s == 'Y' else 0
    sugar_price_per_cube = 5

    ulink_discount = 0.8 if get_input("Are you a Ulink student? Y or N: ", ['Y', 'N']) == 'Y' else 1.0

    base_price = sizes[size] + milk_types[milk] + extra_shot_price + sugar * sugar_price_per_cube
    final_price = get_price_and_apply_discount(base_price, ulink_discount)

    print(f"Your final bill is {final_price}")


try:
    calculate_price()
except KeyboardInterrupt:
    print("\nExit")
