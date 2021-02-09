#! python3
# regexStrip.py
# ABSP - Chapter 7


def strip_regex(text, x):
    """
    Summary:
        Python str.strip() method implemented with Regex.

    Args:
        text (str): Text to strip of variable.
        x (str): Variable to use for the strip.
    Returns:
        strippedText (str): Text stripped of variable.

    """
    import re
    # If string starts or ends whith whitespace.
    # Replaces whitespace with nothing.
    if x == '':
        stripWhiteSpace = re.compile(r'^(\s)*|(\s)*$')              
        strippedText = stripWhiteSpace.sub('', text)           
    # If string starts or ends whith variable 'x'.  
    # Replaces variable 'x' with nothing.
    else:
        stripOther = re.compile(rf'^({x})*|({x})*$')     
        strippedText = stripOther.sub('', text)      

    print(strippedText)
    return strippedText


if __name__ == '__main__':

    text = 'SpamSpamBaconSpamEggsSpamSpam'

    strip_regex(text, 'Spam')