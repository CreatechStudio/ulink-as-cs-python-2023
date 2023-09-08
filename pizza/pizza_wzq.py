# constants
size_prices = {
    'S': 150,
    'M': 200,
    'L': 250,
}

# classes
class Option:
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

    def value(self, size):
        return self.prize[size]

    def get_info(self, size):
        return f'{self.name}: {self.prize[size]}'

class Order:
    def __init__(self, size: int, options: list):
        self.size = size
        self.options = options
        self.price = size_prices[self.size]

    def get_total_prize(self):
        return self.price + sum([opt.value(self.size) for opt in self.options])

    def get_info(self):
        s = f'Pizza {self.size}: {self.price} RMB'
        for i in self.options:
            s += '\n' + i.get_info(self.size) + ' RMB'
        return s

# functions
def choose(q, choices, default):
    low = set()
    for i in range(len(choices)):
        if choices[i] == default:
            choices[i] = choices[i].upper()
        else:
            choices[i] = choices[i].lower()
        low.add(choices[i].lower())

    s = '/'.join(choices)

    result = input(f'{q} [{s}] ').strip().lower()

    if result == '':
        return default.upper()

    if result in low:
        return result.upper()
    else:
        raise ValueError(f'No Choice of {result}. ')

# main
while 1:
    try:
        print('Welcome to Python Pizza Deliveries!')
        # size
        size = choose('What size pizza do you want?', ['S', 'M', 'L'], 'S')
        # options
        options = []
        if choose('Do you want pepperoni? ', ['Y', 'N'], 'N') == 'Y':
            options.append(Option('Pepperoni', {'S': 20, 'M': 30, 'L': 30}))
        if choose('Do you want extra cheese? ', ['Y', 'N'], 'N') == 'Y':
            options.append(Option('Cheese', {'S': 10, 'M': 10, 'L': 10}))

        # calc
        order = Order(size, options)
        print(f'\nOrder Info: \n\033[1m{order.get_info()}\033[0m\n')
        print(f'Total Prize is: \033[1m{order.get_total_prize()} RMB\033[0m')
        print('\n')
    except Exception as e:
        print(e)
