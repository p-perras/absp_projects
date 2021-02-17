#! python3
# emailer.py
# ABSP - Chapter 12

import sys
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def emailer(sendFrom, password, sendTo, message):
    """ 
    Summary:
        Sends message to email address
    Args:
        sendFrom(str): senders email address
        password(str): senders password
        sendTo (str): receipient email address
        message (str): message to send
    Returns:
        None
    """

    # Verify e-mail
    emailReg = re.compile(
        r"""(
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
        )""",
        re.VERBOSE,
    )

    if not emailReg.match(sendTo):
        print("Invalid e-mail adress provided")
    else:
        delay = 15 # seconds

        # set up selenium browser
        browser = webdriver.Chrome()
        browser.get("https://login.yahoo.com/")

        # Enter yahoo e-mail adress
        loginUsernameElem = browser.find_element_by_id("login-username")
        loginUsernameElem.send_keys(sendFrom)

        # Press 'Next' to go to pasword page
        nextBtnElem = browser.find_element_by_id("login-signin")
        nextBtnElem.send_keys(Keys.ENTER)

        # Wait for 'password' field page to load then enter password, tab to submit btn
        time.sleep(delay)  # TO-DO: Replace with a wait_for_load function
        loginPwdElem = browser.find_element_by_id("login-passwd")
        loginPwdElem.send_keys(password)
        loginPwdElem.send_keys(Keys.TAB)

        # Select 'sign-in' btn, press ENTER
        signInBtnElem = browser.find_element_by_id("login-signin")
        signInBtnElem.click()

        # Click on link to redirect to mail.yahoo.com
        mailLinkElem = browser.find_element_by_id("header-mail-button")
        mailLinkElem.send_keys(Keys.ENTER)

        # Click on 'compose' btn
        time.sleep(delay)
        composeBtnElem = browser.find_element_by_link_text("Compose")
        composeBtnElem.send_keys(Keys.ENTER)

        # Use 'time.sleep' to wait instead of 'wait_for..', cause of refreshing issue
        time.sleep(delay)
        
        # Enter email address
        messageToElem = browser.find_element_by_id("message-to-field")
        messageToElem.send_keys(sendTo)

        # Enter Subject
        messageSubjectElem = browser.find_element_by_css_selector(
            'input[placeholder="Subject"]'
        )
        messageSubjectElem.send_keys("FYI")

        # Enter email body
        messageBodyElem = browser.find_element_by_css_selector("div[data-test-id='rte']")
        messageBodyElem.send_keys(message)

        # Send email
        sendBtnElem = browser.find_element_by_css_selector("button[data-test-id='compose-send-button']")
        sendBtnElem.click()
        browser.close()

        print('Message Sent!')


if __name__ == '__main__':

    if len(sys.argv) > 2:
        sendTo = sys.argv[1]
        message = " ".join(sys.argv[2:])

        sendFrom = input("Enter your yahoo-mail email: ")
        password = input("Enter your yahoo-mail password: ")

        emailer(sendFrom, password, sendTo, message)

    elif len(sys.argv) == 2:
        print("Missing message to send")

    else:
        print('Add command line args "e-mail address" and "message".')