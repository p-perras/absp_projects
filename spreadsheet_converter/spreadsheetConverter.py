#! python3
# spreadsheetConverter.py
# ABSP - CHapter 14


import ezsheets


def spreadsheetConverter(fileName, fileFormat):
    """
    Summary:
        Uploads a file to google sheets 
        then downloads it to the specified format.

    Args:
        fileName (str): name of the file to upload.
        format (str): name of file format to convert to.
    """
    ss = ezsheets.upload(fileName)

    if fileFormat.lower() == "excel":
        ss.downloadAsExcel()
    elif fileFormat.lower() == "pdf":
        ss.downloadAsPDF()
    elif fileFormat.lower() == "ods":
        ss.downloadAsODS()
    elif fileFormat.lower() == "csv":
        ss.downloadAsCSV()
    elif fileFormat.lower() == "html":
        ss.downloadAsHTML()
    elif fileFormat.lower() == "TSV":
        ss.downloadAsTSV()


if __name__ == "__main__":
    spreadsheetConverter("produceSales 2.xlsx", "PDF")