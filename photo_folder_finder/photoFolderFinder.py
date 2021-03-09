#! python3
# ABSP - Chapter 18

from PIL import Image
import os

def find_folder(root):
    """
    Summary:
        Walks through root looking for photos folders.

    Args:
        root (string): Root directory to start the search.
    """
    print("Starting Search..")

    for foldername, subfolders, filenames in os.walk("root"):
        numPhotoFiles = 0
        numNonPhotoFiles = 0

        for filename in filenames:
            # Check if file extension is not .png or .jpg
            if not filename.lower().endswith(".png") or filename.lower().endswith(".jpg"):
                numNonPhotoFiles += 1
                continue  # Skip to next filename

            # Open file with Pillow
            im = Image.open(os.path.join(foldername, filename))

            width, height = im.size

            # Check if width and height are larger than 500.
            if width >= 500 and height >= 500:
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is to small to be considered a photo.
                numNonPhotoFiles += 1

        # If more than half of files are photos print abs path to foler.
        if numPhotoFiles > numNonPhotoFiles:
            print(os.path.abspath(foldername))
    print("Done.")
    
if __name__ == "__main__":
    find_folder("/")