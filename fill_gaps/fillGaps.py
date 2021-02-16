#! python3
# fillGaps.py
# ABSP - Chapter 10

import os
import shutil
import re


def fill_gaps(folder, prefix):
    """
    Summary:
        Fills gaps in file numbering in a given folder.

    Args:
        folder (str): Folder path to search for gaps.
        prefix (str): Prefix of files to fill gaps.
    """
    # Make sure folder path is absolute.
    folder = os.path.abspath(folder)

    reg = re.compile(rf'^({prefix})(.*)(\..*)$')
    # Files sorted ascending order.
    fileList = sorted(
        [file for file in os.listdir(folder) if reg.match(file)])

    # Max length of largest number, for padding zeros.
    maxLength = len(reg.match(fileList[-1]).group(2))

    # start with the minimum number in list.
    start = int(reg.match(fileList[0]).group(2))
    count = start

    print(f'Reordering files in {folder}...')
    for file in fileList:

        fileNum = int(reg.match(file).group(2))
        ext = reg.match(file).group(3)
        filePath = os.path.join(folder, file)

        # Loop through files and rename without gaps.
        if fileNum != count:

            newFile = prefix + '0' * (maxLength-len(str(fileNum))) + str(count) + ext
            newFilePath = os.path.join(folder, newFile)
            shutil.move(filePath, newFilePath)

        count += 1

    print('Done!')


if __name__ == '__main__':

    fill_gaps('.', 'spam')
