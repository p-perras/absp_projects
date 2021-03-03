#! python3
# excelToCsv.py
# ABSP - Chapter 16

import openpyxl
import csv
import os

def excel_to_csv(directory):
    """
    Summary:
        Converts all sheets in each excel file in a folder to a csv.
    Args:
        directory (str): Folder containing excel files.
    Returns:
        None
    """
    for excelFile in os.listdir(directory):
        # Skip non .xlsx files, load workbook
        if not excelFile.endswith(".xlsx"):
            continue
        wb = openpyxl.load_workbook(excelFile)

        # Loop through every sheet in the workbook
        for sheetName in wb.sheetnames:
            sheet = wb[sheetName]

            # Create CSV filename from EXCEL filename and sheet title.
            filename = excelFile.split(".")[0] + "_" + sheet.title + ".csv"
            csvFileObj = open(filename, "w", newline="")

            # Create the csv.writer object for this CSV file.
            csvWriter = csv.writer(csvFileObj)

            # Loop through every row in sheet
            for rowObj in sheet.rows:
                rowData = []
                # Loop through each cell in row.
                for cellObj in rowObj:
                    # Append each cell's data to rowData.
                    rowData.append(cellObj.value)
                # Write the rowData list to the CSV file.
                csvWriter.writerow(rowData)
                
            csvFileObj.close()

if __name__ == "__main__":
    excel_to_csv('.')