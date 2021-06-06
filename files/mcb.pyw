"""
Saves and loads pieces of text to the clipboard.
Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list - Loads all keywords to clipboard.
"""

import shelve
import pyperclip
import sys

with shelve.open('mcb') as mcb_shelf:
    # Save clipboard content
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        key = sys.argv[2]
        mcb_shelf[key] = pyperclip.paste()
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
