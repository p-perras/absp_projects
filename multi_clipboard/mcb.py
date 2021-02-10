#! python3
# mcb.py 
# ABSP - Chapter 9

import sys
import pyperclip
import shelve

"""
Usage:
    python3 mcb.py save <keyword> - Saves clipboard to keyword.
    python3 mcb.py <keyword> - Load keyword to clipboard.
    python3 mcb.py list - Loads all keywords to clipboard.
    python3 mcb.py delete <keyword> - Delete keyword from shelf
    python3 mcb.py delete_all - Delete all keywords from shelf
"""
# Open new shelf file.
mcbShelf = shelve.open('mcb')
# Command variable for ease of code.
command = sys.argv[1].lower()

if command == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif command == 'list':
    pyperclip.copy(', '.join(mcbShelf.keys()))
elif command == 'delete':
    del mcbShelf[sys.argv[2]]
elif command == 'delete_all':
    mcbShelf.clear()
else:
    pyperclip.copy(mcbShelf[sys.argv[1]])

# Close shelf file.
mcbShelf.close()