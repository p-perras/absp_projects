#! python3
#! ABSP - Chapter 18

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catLogo.png"

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# List of possible extensions.
extList = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]

os.makedirs("withLogo", exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir("."):
    # Split filename
    ext = os.path.splitext(filename)[1].lower()
    if not ext in extList or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself.

    im = Image.open(filename)
    width, height = im.size

    # Check if image need to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print(f"Resizing {filename}...")
        im = im.resize((width, height))

    # Check if logo fits properly.
    imWidth, imHeight = im.size
    if imWidth < logoWidth * 2 and imHeight < logoHeight * 2:
        print(f"Logo takes up too much space on {filename} so skipped..")
    # Add the logo.
    else:
        print(f"Adding logo to {filename}...")
        # paste() method will not paste the transparency pixels if you do not
        # pass the logoIm for the third argument as well.
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save the changes.
    im.save(os.path.join("withLogo", filename))

