#! python3
# chapter_10.py - Prints the abspath of files or folders over a certain size in a folder

import os
import pyinputplus as pyinp


def find_unneeded(folder, mb):
    """
    Summary:
        Walks through a folder tree and searches for exceptionally large files

    Args:
        folder (str): Folder path to walk through.
        mb (int): File size in megabytes to reject.

    Returns:
        to_delete (dict): dictionnary of file paths to delete.
    """
    # Empty dictionnary for files to delete
    to_delete = {}

    # Make sure folder path is absolute
    folder = os.path.abspath(folder)

    print(f'Getting file sizes from {folder}...')
    # Walk the entire folder tree and and get file sizes
    for folderName, subFolder, fileName in os.walk(folder):
       
        # Handle errors.
        try:
            for file in fileName:
                filePath = os.path.join(folderName, file)
                
                # 1 MB = 1000000 Bytes
                fileSize = os.path.getsize(filePath) / 1000000

                # Checks if file size is over argument size
                # And adds the filePath and size in to_delete
                if fileSize > mb:
                    to_delete[filePath] = round(fileSize, 1)
                    print(f'{file}: {round(fileSize, 1)}MB')
        except FileNotFoundError as error:
            print(error)

    if not to_delete:
        print(f'No files over {mb}MB ')

    # Option to delete files.
    else:
        to_trash = pyinp.inputYesNo(
            'Would you like to delete All theses files? (Yes / No) ')
        if to_trash.lower() == 'yes':
            for k in to_delete.keys():
                # Uncomment to enable send2trash
                # send2trash.send2trash(k)
                print(f'{k} deleted')
            print('Files deleted.')

        else:
            print('Program ended.')


if __name__ == '__main__':

    find_unneeded('.', 100)
