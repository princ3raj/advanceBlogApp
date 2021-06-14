import requests
import os

import bs4


url = 'https://www.youtube.com/live_chat?continuation=0ofMyANxGlhDaWtxSndvWVZVTmtOREJqVGtKMFQwVnhaVmRNTW5wNk5FaE9VMkZSRWd0eGRubFVlREF4V21OUlVSb1Q2cWpkdVFFTkNndHhkbmxVZURBeFdtTlJVU0FCMAGCAQIIBIgBAaABi7Lt6PLX7wKyAQA%253D'

req = requests.get(url)


try:
    req.raise_for_status()
except Exception as e:
    pass
else:
    # soup = bs4.BeautifulSoup(req.text, 'html.parser')

    file = open('youtube.html', 'wb')

    for text in req.iter_content(100000):
        file.write(text)
