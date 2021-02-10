#! python3
# sandwichMaker.py
# ABSP - Chapter 8


def make_sandwiches():
    """
    Summary:
        Takes inputs for sandwich preferences and displays final cost.
    """
    import pyinputplus as pyip
    choices = []
    total_cost = 0

    # Dictionary of products and prices
    price_list = {
        'Wheat': 3, 'White': 3, 'Sourdough': 3.5,
        'Chicken': 1, 'Turkey': 1, 'Ham': 1, 'Tofu': 1.5,
        'Cheddar': 1, 'Swiss': 1.5, 'Mozzarella': 0.5, 'None': 0
    }

    # Bread selection
    bread_type = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
    choices.append(bread_type)

    # Protein selection
    protein_type = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
    choices.append(protein_type)
    # Cheese seletction
    if pyip.inputYesNo('Would you like cheese? ("yes" or "no")') == 'yes':
        cheese_type = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
        choices.append(cheese_type)
    else:
        cheese_type = 'None'

    # Condiment selection
    if pyip.inputYesNo('Would you like condiments? ("yes" or "no")') == 'yes':
        condiments = pyip.inputMenu(
            ['Mayo', 'Mustard', 'Lettuce', 'Tomato'], numbered=True)

    # Calculate sandwiche cost
    for item in choices:
        total_cost += price_list[item]

    # Number of sandwiches
    number_sandwiches = pyip.inputInt('How many sandwiches would you like?', min=1)

    # Print total cost
    print(f'''Your sandwich's price is ${float(total_cost)}.
    Your total cost will be ${float(total_cost * number_sandwiches)}
    ''')


if __name__ == '__main__':
    make_sandwiches()