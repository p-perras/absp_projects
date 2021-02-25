#! python3
# downloadGoogleFormData.py
# ABSP - Chapter 14

import ezsheets


def get_form_data(fileName):
    """
    Summary:
        Collects e-mail adresses from a Google Sheet containing the responses of a form.

    Args:
        fileName (str): Google spreadsheet name or ID

    Returns:
        List of e-mail Adresses
    """
    ss = ezsheets.Spreadsheet(fileName)
    sheet = ss[0]

    emailCol = 0
    emailList = []

    # Find row number for 'Adresse e-mail'.    
    for i, value in enumerate(sheet.getRow(1)):
        # Sheet is in French, change 'Adresse e-mail' if Sheet is in English
        if value == 'Adresse e-mail':
            emailCol = i + 1

    # Append emails to emailList.
    for value in sheet.getColumn(emailCol)[1:-1]:
        if value != '':
            emailList.append(value)
    
    print(emailList)
    return emailList


if __name__ == '__main__':
    get_form_data('Contact Info Results')
