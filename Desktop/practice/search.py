#! python3
# search.py - Opens several Google search results.
import time
import requests
import sys
import webbrowser
import bs4
print('Googling...')  # display text while downloading the Google page
res = requests.get('https://www.google.co.in/search?q=' +
                   ' '.join(sys.argv[1:]))


try:

    res.raise_for_status()
except Exception as e:
    print(f'There is an error: {e}')
else:

    # TODO: Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # TODO: Open a browser tab for each result.
    linkElems = soup.find_all('a')

    file = open('index.html', 'w')
    for chunk in linkElems:
        file.write(str(chunk))

    file.close()

    # for item in linkElems:
    #     if 'educative' in item:
    #         print(True)

    # numOpen = len(linkElems)
    # for i in range(numOpen):

    #     webbrowser.open(linkElems[i].get('href'))
