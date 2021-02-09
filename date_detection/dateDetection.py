#! python3
# dateDetection.py
# ABSP - Chapter 7


def date_detecter(date):
    """
    Summary:
        Verfifies if a date is valid, taking in leap years.

    Args:
        date (str): Date in the dd/mm/yyyy format

    Returns:
        [str]: A string informing if the date is valid.
    """
    import re

    # Regex.
    dateRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')
    # Validate format.
    while True:
        if dateRegex.search(date) is None:
            print('Invalid Format')
            date = input('Insert date in format dd/mm/yyyy : ')
        else:
            break

    # Assign variables named month, day, year.
    # Change single digit to doubles.
    day, month, year = dateRegex.search(date).groups()
    if len(day) != 2:
        day = '0' + day
    if len(month) != 2:
        month = '0' + month


    # Function to check if leap year.
    def is_leap_year(data):
        year = int(data)
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


    # Date validation and print.
    valid_date = f'After verification, {day}-{month}-{year} is a valid Date.'
    invalid_date = f'After verification, {day}-{month}-{year} is NOT a valid Date.'

    if month in ['04', '06', '09', '11'] and int(day) <= 30:
        print(valid_date)
    elif month == '02' and is_leap_year(year) and int(day) <= 29:
        print(valid_date)
    elif month == '02' and not is_leap_year(year) and int(day) <= 28:
        print(valid_date)
    elif month in ['01', '03', '05', '07', '08', '10', '12'] and int(day) <= 31:
        print(valid_date)
    else:
        print(invalid_date)


if __name__ == '__main__':
    date = input('Insert date in format dd/mm/yyyy : ')
    date_detecter(date)