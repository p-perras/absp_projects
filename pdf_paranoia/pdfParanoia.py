#! python3
# pdfParanoia.py
# ABSP - Chapter 15

import PyPDF2
import os


def encryptPDFs(directory, password):
    """
    Summary:
        Walks through directory and encrypts all PDF files.
        Stores files in a folder called 'encrypted'

    Args:
        directory (str): directory to search: path.
        password (str): password to encrypt the PDF files with.
    """
    # Set folder path for encrypted files
    folderPath = os.path.abspath(os.path.join(directory, 'encrypted_files'))
    os.makedirs(folderPath, exist_ok=True)


    for Folder, Subfolders, Files in os.walk(directory):
        
        for file in Files:
            
            if file.endswith('.pdf'):
                filePath = os.path.join(os.path.abspath(Folder), file)
                pdfFileObj = open(filePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

                # If not encrypted, encrypt.
                if not pdfReader.isEncrypted:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    pdfWriter.encrypt(password)

                    # New file name and path.
                    newFile = '_encrypted.'.join(os.path.basename(filePath).split('.'))
                    newPath = os.path.join(folderPath, newFile)

                    #Write encrypted file.
                    outputPdf = open(newPath, 'wb')
                    pdfWriter.write(outputPdf)
                    outputPdf.close()
                pdfFileObj.close()

    print('Done.')


def decryptPdfs(directory, password):
    """
    Summary:
        Walks through directory and decrypts all PDF files.
        Stores files in a folder called 'decrypted'

    Args:
        directory (str): directory to search: path.
        password (str): password to decrypt the PDF files with.
    """
    folderPath = os.path.abspath(os.path.join(directory, 'decrypted_files'))
    os.makedirs(folderPath, exist_ok=True)

    for Folder, Subfolders, Files in os.walk(directory):
        
        for file in Files:
            
            if file.endswith('_encrypted.pdf'):
                filePath = os.path.join(os.path.abspath(Folder), file)
                pdfFileObj = open(filePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

                # Decrypt with provided password.
                succes = pdfReader.decrypt(password)

                if succes:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    
                    # New file name and path.
                    newFile = ''.join(os.path.basename(filePath).split('_encrypted'))
                    newPath = os.path.join(folderPath, newFile)
                    
                    # Write decrypted file.
                    outputPdf = open(newPath, 'wb')
                    pdfWriter.write(outputPdf)
                    outputPdf.close()
                
                else:
                    print(f'Wrong Password for: {file}')
                pdfFileObj.close()


if __name__ == "__main__":
    password = input('Enter encryption password: ')
    method = input('"Encrypt" or "Decrypt"? ')
    if method.lower() == 'encrypt':
        encryptPDFs('/Users/philippe/Desktop/Emma', password)
    elif method.lower() == 'decrypt':
        decryptPdfs('/Users/philippe/Desktop/Emma', password)
    else:
        print('Insert "encrypt" or "decrypt": ')
