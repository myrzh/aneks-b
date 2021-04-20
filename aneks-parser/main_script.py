# https://nekdo.ru/page/n         n is the page number, at least 3717

from bs4 import BeautifulSoup
import os


path, dirs, files = next(os.walk("pages"))
num_of_pages = len(files)
dates = []
texts = []
mydivs_temp = []
mydivs = []
aneks = open('aneks.txt', 'w', encoding="utf8")

for page in range(1, num_of_pages + 1):
    with open("pages/" + str(page) + ".html", "r", encoding="utf8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        mydivs_temp = soup.find_all("div", {"class": "text"})
        for i in mydivs_temp:
            mydivs.append(i)

for i in range(0, len(mydivs)):
    mydivs[i] = str(mydivs[i])
    mydivs[i] = mydivs[i][mydivs[i].find(">") + 1:-6]
    mydivs[i] = mydivs[i].replace('<br/>', ' ')
    print(mydivs[i])
    print()

for i in mydivs:
    aneks.write(i + "\n")
    aneks.write("\n")
aneks.close()
