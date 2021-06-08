"""
Automatically launch the map in your browser using the contents of your clipboard.
The programm is set to open a web browser to 'https://
www.google.com/maps/place/your_address_string' (where your_address_string is
the address you want to map).
"""

import webbrowser
import sys
import pyperclip

# Get address from the command line
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
