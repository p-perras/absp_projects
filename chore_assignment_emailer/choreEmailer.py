#! python3
# choreEmailer.py
# ABSP - Chapter 18

import smtplib
import pyinputplus as pyip
import random


def emailer(chores, emails):
    """
    Summary:
        Emails random chores to emails with gmail.

    Args:
        chores (list): list of chores.
        emails (dict): dictionnary containning names, emails and last chore.
    """
    # Assign Chore to 'emails'
    for name in emails.keys():
        randomChore = random.choice(chores)
        emails[name]['chore'] = randomChore
        chores.remove(randomChore) # this chore is now taken, so remove it
    
    # Email account details.
    email = input('Enter your email: ')
    password = pyip.inputPassword('Your Password: ')

    # Log in to email
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email, password)
    # See https://support.google.com/accounts/answer/6010255 if (Bad Credentials Error)

    # Send chore email
    for name in emails:
        email = emails[name]['email']
        chore = emails[name]['chore']
        body = f""" Subject: This Week's Chore.
        \nDear {name},
        \nYour assigned chore for this week is: {chore}.
        \nThank you and have a nice week!"""

        print(f'Sending email to {name}...')
        sendmailStatus = smtpObj.sendmail('1philippe.perras1@gmail.com', email, body)

        if sendmailStatus != {}:
            print(f'There was a problem sending email to {email}: {sendmailStatus}')
    
    # Log out
    smtpObj.quit()
    print('Done.')


if __name__ == '__main__':
    chores = ['Vaccum Floor', 'Clean Fridge']
    emails = {'John': {'email': 'johndoe@example.com', 'chore': ''}}   
    
    emailer(chores, emails)