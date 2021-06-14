# • Download pages with the requests module.
# • Find the URL of the comic image for a page using Beautiful Soup.
# • Download and save the comic image to the hard drive with iter_content().
# • Find the URL of the Previous Comic link, and repeat.


import requests
import os
import bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    req = requests.get(url)

    try:
        req.raise_for_status()
    except Exception as e:
        print(f'{e}')
    else:
        bs = bs4.BeautifulSoup(req.text, 'html.parser')
        bs.prettify()
        image = bs.select('#comic img')
        if not image:
            print("Image not available")
        else:
            comicURL = image[0].get('src')
            Image = requests.get('https:'+comicURL)
            imageFile = open(os.path.join(
                'xkcd', os.path.basename(comicURL)), 'wb')
            for chunk in Image.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # Get the Prev button's url.
        prevLink = bs.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        print(url)
