#! python3
# commaCode.py
# ABSP - Chapter 4

def comma_code(items):
    """
    Summary:
        Combines list into a string of the form item1, item2, and item3.

    Args:
        items (list): List of strings.

    Returns:
        str: List items combined into a string.
    """
    if len(items) == 0:
        return ''

    elif len(items) == 1:
        return items[0]

    return ', '.join(items[:-1]) + ', and ' + items[-1]


if __name__ == '__main__':   
    spam = ['apples', 'bananas', 'tofu', 'cats']
    result = comma_code(spam)
    print(result)