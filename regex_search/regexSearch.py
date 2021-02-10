#! python3
# regexSearch.py
# ABSP - Chapter 9

import re
import os


def regex_search(regex, folderPath):
    """
    Summary:
        Opens all .txt files in a folder and searches for 
        any line that matches a user-supplied regular expression.

    Args:
        regex (str): Word to search.
        folderPath (str): Folder path to search.
    """
    # Test if folderPath is valid.
    if not os.path.isdir(folderPath):
        print('Invalid directory path.')
        return
    
    # Complie user provided regex to search.
    reg = re.compile(regex)

    # Loop through all .txt files.
    for filename in os.listdir(folderPath):
        if filename.endswith('.txt'):
            with open(filename) as file:

                for line in file:
                    # If match, prints to console.
                    if reg.search(line):
                        print(f'{filename} contains: \n', line)


if __name__ == '__main__':

    regex = input('Enter regex to search: ')
    folderPath = input('Enter folder path to search: ')
    regex_search(regex, folderPath)