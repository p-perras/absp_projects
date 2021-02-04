# !python3
# collatz.py
# ABSP - Chapter 3

def collatz(number):
    """
    Summary:
        If number is even (number // 2) else (3 * number + 1)
    Args:
        number (int): Number to collatz.
    Returns:
        int: Collatz number.
    """
    if number % 2 == 0:
        print(number // 2)
        return (number // 2)
    else:
        print(3 * number +1)
        return(3 * number + 1)
    

if __name__ == '__main__':
    try:
        number = int(input('Enter a number: '))
        result = collatz(number)
        while result != 1:
            result = collatz(result)
    except ValueError:
        print('You di not enter a valid number.')