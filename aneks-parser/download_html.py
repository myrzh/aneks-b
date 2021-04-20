# https://nekdo.ru/page/n         n is the page number, at least 3717

import urllib.request
import time


url = 'https://nekdo.ru/page/' # hardcoded
num = 3717 # hardcoded

for page in range(1, num + 1):
    url += str(page)
    with urllib.request.urlopen(url) as url:
        html = url.read()
    f = open('pages/' + str(page) + '.html', 'wb')
    f.write(html)
    print('Page ' + str(page) + ' downloaded!')
    url = 'https://nekdo.ru/page/'
