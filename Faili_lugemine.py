from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.rimi.ee/epood/ee/tooted/alkohol/c/SH-1?currentPage=1&pageSize=80&query=%3Arelevance%3AallCategories%3ASH-1%3AassortmentStatus%3AinAssortment"
page = urlopen(url)
html = page.read().decode("utf-8")
Prisma_olu = BeautifulSoup(html, "html.parser")
olud = open("Olud.txt", "w", encoding="utf-8")
olud.write(Prisma_olu.get_text())
olud.close()
hinnad_olu = open("hinnad_olu.txt", "w")
