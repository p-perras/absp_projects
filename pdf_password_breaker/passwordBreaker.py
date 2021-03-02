#! python3
# passwordBreaker.py
# ABSP - Chapter 15


import PyPDF2


def break_password(pdfFile, dictionnary):
    """
    Summary:
        breaks a single word password for a PDF
    Args:
        pdfFile (str): filename of the encrypted PDF
        dictionnary (str): filename of dictionnary of words to use

    Returns:
        (str): password
    """
    pdfFile = open(pdfFile, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    with open(dictionnary) as wordList:
        for word in wordList.read().split("\n"):

            wordLower = word.lower()
            wordCap = word.capitalize()

            if pdfReader.decrypt(word):
                print(f"Password is: {word}")
                return word
            elif pdfReader.decrypt(wordLower):
                print(f"Password is: {wordLower}")
                return wordLower
            elif pdfReader.decrypt(wordCap):
                print(f"Password is {wordCap}")
                return wordCap


if __name__ == "__main__":
    break_password("encrypted.pdf", "dictionary.txt")

