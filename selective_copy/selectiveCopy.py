#! python3
# selectiveCopy.py
# ABSP - Chapter 10

import os
import shutil


def selective_copy(folder, extension):
    """
    Summary:
        Walks through a folder tree and searches for files with a specified file extension, copies them into new folder.

    Args:
        folder (str): Path of folder to walk through.
        extension (str): File extension to search for.

    Returns:
        [str]: New folder path.
    """
    # Make sure folder path is absolute
    folder = os.path.abspath(folder)

    # Figure out the folder name this code should use based on
    # what folders already exist.
    number = 1
    while True:
        outFolder = 'result_' + extension.lower() + '_' + str(number)
        outFolder = os.path.join(folder, outFolder)
        if not os.path.exists(outFolder):
            break
        number = number + 1

    # Create new folder.
    print(f'Creating new folder: {outFolder}...')
    os.mkdir(outFolder)

    # Walk the entire folder tree and copy the files to new folder.
    for folderName, subFolder, fileName in os.walk(folder):
        print(f'Searching for {extension.upper()} files in {folderName}...')

        # Prevent copying from new folder.
        if folderName == outFolder:
            continue

        for file in fileName:
            # Get full, absolute file path.
            filePath = os.path.join(os.path.abspath(folderName), file)
            # Copy if file extension matches what we are looking for.
            if filePath.endswith(extension):
                shutil.copy(filePath, outFolder)

    print('Done!')
    return outFolder


if __name__ == '__main__':
    selective_copy('.', 'pdf')
