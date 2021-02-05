#! python3
# fantasyGameInventory.py
# ABSP - Chapter 5


def display_inventory(inventory):
    """
    Summary:
        Displays what the play has in inventory.

    Args:
        inventory (dict): Inventory conainning items and their counts.
    """

    print('Inventory: ')
    for k, v in inventory.items():
        print(f'{v} {k}')

    item_total = 0
    for v in inventory.values():
        item_total += v
    
    print(f'Total number of items: {item_total}')


def add_to_inventory(inventory, addedItems):
    """
    Summary:
        Adds items to inventory.    

    Args:
        inventory (dict): Inventory conainning items and their counts.
        addedItems (list): Items to add to inventory.

    Returns:
        updatedInventory (dict): Inventory with added items.
    """
    updatedInventory = dict(inventory)

    for looted_item in addedItems:
        updatedInventory.setdefault(looted_item, 0)
        updatedInventory[looted_item] += 1

    return updatedInventory


if __name__ == '__main__':

    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)