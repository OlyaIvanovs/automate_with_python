"""
This programm allows type a search term on the com-
mand line and have a computer automatically open a browser with all
the top search results in new tabs.
"""

import sys
import webbrowser
import bs4
import requests
import pyperclip

print("Googling...")
# Get search term from command line
if len(sys.argv) > 1:
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # pyperclip.copy(str(soup)) If you want to see result of scraping

    link_elems = soup.select('.kCrYT a')
    num_open = min(5, len(link_elems))
    # Open a browser tab for each result.
    for i in range(num_open):
        print(link_elems[i])
        webbrowser.open('http://google.com' + link_elems[i].get('href'))
