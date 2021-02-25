#! python3
# mistakeFinder.py
# ABSP - Chapter 14 

import ezsheets


def mistakeFinder(fileName):
    """
    Summary:
        Searches a google sheet for multiplication errors

    Args:
        fileName (str): google sheet file ID to search
    Returns:
        None

    """
    ss = ezsheets.Spreadsheet(fileName)
    sheet = ss[0]

    errors = []

    max_row = 0

    # Find max row
    for row in range(1, sheet.rowCount):
        if sheet.getRow(row)[0] == "":
            max_row = row
            break

    for i in range(2, max_row):
        A = int(sheet.getRow(i)[0])
        B = int(sheet.getRow(i)[1])
        C = int(sheet.getRow(i)[2])

        if A*B != C:
            errors.append(i)

    if len(errors) == 0:
        print('No errors were found')
    else:
        print(f'Errors were found in these rows: {errors}')

if __name__ == '__main__':
    mistakeFinder('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')