# !python3
# strongPasswordDetector.py
# ABSP - Chapter 7


def test_password(password):
    """
    Summary:
        Tests a password for theses conditions:
        - contains at least eight characters.
        - contains both uppercase and lowercase characters. 
        - contains at least one digit.

    Args:
        password (str): Password to test.

    Returns:
        (bool): True if password is strong enough, else False.
    """
    import re

    # Regex length.
    length_regex = re.compile(r'[\w\d\s\W\D\S]{8,}')
    # Regex for strength.
    pass_regex = re.compile(r'[A-Z]+[a-z]+[\d]+')

    # Test regex.
    if not length_regex.search(password):
        print('Password NOT long enough.')
        return False
    elif not pass_regex.search(password):
        print('Password NOT strong enough.')
        return False
    print('Password strong enough!')
    return True


if __name__ == '__main__':
    pw = 'aP9koLp0j$'
    test_password(pw)