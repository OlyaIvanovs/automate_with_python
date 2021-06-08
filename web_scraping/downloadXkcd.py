"""Downloading comics from http://xkcd.com/"""

import re
import requests
import os
import bs4

url = 'http://xkcd.com'
os.makedirs("xkcd", exist_ok=True)

while not url.endswith('#'):
    # Download the page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    # Find the URL of the image
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    imgs = soup.select('#comic img')
    if imgs == []:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + imgs[0].get('src')
        print(comic_url)
        # Download and save image
        print("Downloading image...")
        res = requests.get(comic_url)
        res.raise_for_status()
        file_path = os.path.join('xkcd', os.path.basename(comic_url))
        with open(file_path, 'wb') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)

    # Find prev button
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print("Done")
