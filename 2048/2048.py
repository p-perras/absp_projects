#! python3
# 2048.py
# ABSP - Chapter 12


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random


def play():
    """
    Args:
        None
    Returns:
        None
    """
    # set up selenium browser
    browser = webdriver.Chrome()
    browser.get("https://play2048.co/")

    # set up elements
    gameStatusElem = browser.find_element_by_css_selector(".game-container p")
    htmlElem = browser.find_element_by_css_selector("html")

    num_moves = 0
    # set up loop
    while gameStatusElem.text != "Game over!":
        key_select = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
        key = random.randint(0, 3)

        htmlElem.send_keys(key_select[key])

        score = browser.find_element_by_css_selector(".score-container").text
        num_moves += 1

    print(f"Your scored: {score} in {num_moves} moves!")
    browser.close()


if __name__ == "__main__":
    play()
