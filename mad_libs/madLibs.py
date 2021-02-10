#! python3
# madLibs.py
# ABSP - Chapter 9

import re


def mad_libs(inputFile):
    """
    Summary:
        Reads in text files and lets the user add their own text anywhere the word 
        ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

    Args:
        inputFile (str): Name of text file to parse.
    """
    # Regex.
    reg = re.compile(r'(NOUN|ADJECTIVE|ADVERB|VERB)')

    # Open files with a "with" statement for legibilaty.
    with open(inputFile, 'r') as inFile, open('newText.txt', 'w') as outFile:
        text = inFile.read()
        # Matches to replace.
        matches = reg.findall(text)

        for match in matches:
            # Changes the article to proper english.
            article = 'a'
            if match.lower() == 'adjective':
                article = 'an'
            # User input and replace.
            sub = input(f'Enter {article} {match}: ')
            text = text.replace(match, sub, 1)

        # Write to outFile and print.
        outFile.write(text)
        print(text)


if __name__ == '__main__':
    mad_libs('madText.txt')