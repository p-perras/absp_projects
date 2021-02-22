#! python3
# textToSheet.py
# ABSP - Chapter 13

import openpyxl
import os


def textToSheet(directory, fileName):
    """
    Summary:
        Read the contents of several text files and writes them to a spreadsheet
    Args:
        directory (str): folder containing text files
        filename (str): name of excel file
    """
    wb = openpyxl.Workbook()
    sheet = wb.active

    col = 1

    # Change directory
    os.chdir(directory)
    # Loop through files that end with .txt
    for file in os.listdir():
        if file.endswith(".txt"):
            row = 1
            # Open file and write to spreadsheet
            textFile = open(file, "r")
            for line in textFile.readlines():
                sheet.cell(row=row, column=col).value = line
                row += 1
            textFile.close()
            # Add column for next file
            col += 1

    wb.save(fileName)


if __name__ == "__main__":
    textToSheet(".", "text-to-sheet.xlsx")
