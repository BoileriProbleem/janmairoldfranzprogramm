import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.rimi.ee/epood/ee/tooted/alkohol/c/SH-1?currentPage=1&pageSize=80&query=%3Arelevance%3AallCategories%3ASH-1%3AassortmentStatus%3AinAssortment"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
olud = open("Olud.txt", "w", encoding="utf-8")
test = open("Test.txt", "w", encoding="utf-8")
kogu_tekst = soup.get_text()
data = soup.find('script', type='text/plain').get_text()
test.write(data)
for rida in data:
    if rida.strip():
        olud.write(rida)
    elif rida == " ":
        olud.write(rida)
    elif rida == "\t":
        olud.write(rida)
olud.close()
hinnad_olu = open("hinnad_olu.txt", "w")
