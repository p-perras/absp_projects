#! python3
# sheetToTextFile.py
# ABSP - Chapter 13

import openpyxl

def sheetToTextFile(fileName):
    """
    Summary:
        Writes the contents of cells in columns to text files.
    Args:
        fileName (str): name of excel file to use
    """
    # Create workbook and worksheet
    wb = openpyxl.load_workbook(fileName)
    sheet = wb.active

    # Set count for filename
    count = 1
    # Loop through columns
    for colObj in sheet.columns:

        textFile = open('result_file_' + str(count), 'w')
        for cellObj in colObj:
            textFile.write(str(cellObj.value))
        textFile.close()
        
        count += 1

    wb.save(fileName)


if __name__ == '__main__':
    sheetToTextFile('text-to-sheet.xlsx')