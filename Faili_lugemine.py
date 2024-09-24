import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

def andmesaak(test, kokku, eelmineväli, eelmine):
    olud = open("Olud.txt", "a", encoding="utf-8")
    for rida in test:
        if rida[0].isdigit():
            if kokku == False:
                kakskoos = eelmine + "," + rida
                kokku = True
            else:
                olud.write(kakskoos + "," + rida)
                kokku = False
                eelmineväli = False
        elif eelmineväli:
            if kakskoos.find(eelmine) != -1:
                olud.write(kakskoos)
            else:
                olud.write(eelmine)
            eelmineväli = False
            kokku = False
        if rida.find("name") != -1 or rida.find("price") != -1:
            eelmine = rida
            eelmineväli = True
    olud.close()
            
def leht(i):
    url = "https://www.rimi.ee/epood/ee/tooted/alkohol/c/SH-1?currentPage=" + str(i) + "&pageSize=80&query=%3Arelevance%3AallCategories%3ASH-1%3AassortmentStatus%3AinAssortment"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    test = open("Test.txt", "w", encoding="utf-8")
    kogu_tekst = soup.get_text()
    data = soup.find('script', type='text/plain').get_text()
    test.write(data)
    test.close()
    with open("Test.txt", "r", encoding='utf-8') as f:
        test = f.read()
    f.close()
    test = test.split(",")
    return test

    

Gojo = "jap"
Filip = False
Hamlet = False
i = 1
olud = open("Olud.txt", "w", encoding="utf-8")
# olud.close()
lru = "https://www.rimi.ee/epood/ee/tooted/alkohol/c/SH-1?currentPage=" + str(i) + "&pageSize=80&query=%3Arelevance%3AallCategories%3ASH-1%3AassortmentStatus%3AinAssortment"
egap = urlopen(lru)
lmth = egap.read().decode("utf-8")
puos = BeautifulSoup(lmth, "html.parser")
võhandu = open("Test.txt", "w", encoding="utf-8")
for each_div in puos.findAll("main", {"id":"main"}):
    for rida in each_div:
        if rida.find("pagination__item -chevron") != -1:
            olud.write(str(rida))
#while i <= 18:
    #tagastus = leht(i)
    #i += 1
    #andmesaak(tagastus, Hamlet, Filip, Gojo)
    
