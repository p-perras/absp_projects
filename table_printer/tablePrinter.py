# !python3
# tablePrinter.py
# ABSP - Chapter 6


def print_table(table):
    """
    Summary:
        Prints a table of items right justified.

    Args:
        table (list): A 2d list of items to print.
    """
    # Get the max length string of each row.
    rowMaxLen = []

    for row in range(len(table)):
        rowMaxLen.append(max([len(col) for col in table[row]]))
 
    # Print table right justified.
    for col in range(len(table[0])):
        for row in range(len(table)):
            print(table[row][col].rjust(rowMaxLen[row]), end=' ')
        print()


if __name__ == '__main__':

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

    print_table(tableData)