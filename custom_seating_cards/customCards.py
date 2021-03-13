# !python3
# customCards.py
# ABSP - Chapter 18

import os
from PIL import Image, ImageDraw, ImageFont


def make_cards(guestList):
    """
    Summary:
        Makes custom cards for each guest.

    Args:
        guestList (str): Path to a file containing a guest list.
    """
    # Create folder to store images.
    os.makedirs("card_images", exist_ok=True)  

    # Load flower image.
    flowerIm = Image.open("flower.png")

    # Read each guest name from file.
    with open(guestList) as file:
        for line in file:
            guest = line[:-1]

            # Create new image.
            card = Image.new("RGBA", (360, 288), "white")
            # Add flower image.
            card.paste(flowerIm, (0, 0))

            # Create Border.
            draw = ImageDraw.Draw(card)
            draw.rectangle((0, 0, 360, 288), outline="black")

            # Get font.
            pacificoFont = ImageFont.truetype("pacifico.ttf", 24)
            # Get font size for center justification.
            width, height = draw.textsize(guest, font=pacificoFont)

            # Draw guest name.
            draw.text(
                ((360-width) / 2, (288-height) / 2),
                guest,
                fill="black",
                font=pacificoFont,
            )

            # Save image.
            imageName = f"{guest}_card.png"
            card.save(os.path.join("card_images", imageName))


if __name__ == "__main__":
    make_cards("guests.txt")