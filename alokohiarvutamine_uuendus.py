import re
#\u00d5 = "Õ"

def loeb_failist(failinimi):
    joogid = []
    with open(failinimi, "r" , encoding="UTF-8") as fail:
        while True:
            nimerida = file.readline().strip()
            if not nimerida:
                break
            hinnarida = file.readline().strip()
            
            jooginimi = re.search(r'"name": "(.*?), (\d+)%vol, (\d+)ml"', nimerida)
            hinnasumma = re.search(r'"price": (\d+\.?\d*)', hinnarida)
            
            if jooginimi and hinnasumma:
                nimi = name_match.group(1)
                etanool = float(jooginimi.group(2))
                kogus = float(jooginimi.group(3))
                hind = float(hinnasumma.group(1))
                
                joogid.append({
                    "nimi": nimi,
                    "etanool": etanool,
                    "kogus": kogus,
                    "hind": hind
                    })
    return joogid
            
       # reader = csv.DictReader(file)
       # for row in rider
        #    joogid.append({
           #     "nimi" : row["nimi"],
           #     "etanool" : float(row["etanool"]),
            #    "hind" : float(row["hind"]),
            #    "kogus" : float(row["kogus"])
            #    })
         #   return joogid

def soovitud_andmed():
    min_etanool = float(input("sisesta enda minimaalne etanooli soovitud kogus (ml): "))
    max_etanool = float(input("sisesta enda maksimaalne etanooli soovitud kogus (ml): "))
    min_kogus = float(input("sisesta enda minimaalne joogi suurus (ml): "))
    max_kogus = float(input("sisesta enda maksimaalne joogi suurus (ml): "))
    min_hind = float(input("sisesta enda minimaalne hind (€): "))
    max_hind = float(input("sisesta enda maksimaalne hind (€): "))
    
    return min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind
    

            
def parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind):
    sobiv_jook = []
    
    for jook in joogid:
        if (min_etanool <= jook["etanool"] <= max_etanool and
            min_kogus <= jook["kogus"] <= max_kogus and
            min_hind <= jook["hind"] <= max_hind):
            sobiv_jook.append(jook)
    return sobiv_jook
            
def etanooli_arvutus_kogus(jook):
    etanooli_ml = (jook["etanool"] / 100) * jook["kogus"]
    return etanooli_ml

def etanooli_arvutus_hind(jook):
    etanooli_ml = etanooli_arvutus_kogus(jook)
    etanooli_hind_ml_suhtes = jook["hind"] / etanooli_ml
    return etanooli_hind_ml_suhtes

if __name__ == "__main__":
    
    joogid = loe_failist("joogid.txt")
    min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind, soovitud_andmed()
    sobiv_jook = parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind)
    
    if sobiv_jook:
        print("sobib jook: ")
        for jook in sobiv_jook:
            etanooli_hind = etanooli_arvutus_hind(jook)
            print(f"Nimi: {jook['nimi']}, hind: {jook['hind']} €, Etanool: {jook['etanool']} %, Kogus: {jook['kogus']} ml")
            print(f"Etanooli hind (1ml kohta): {etanooli_hind:.4f} €")
    else:
        print("Ei leidnud teile soovitud jooki")
    
-----------------------------------
import re

def loeb_failist(failinimi):
    joogid = []
    with open(failinimi, "r" , encoding="UTF-8") as fail:
        while True:
            nimerida = fail.readline().strip()
            if not nimerida:
                break
            hinnarida = fail.readline().strip()
            
            jooginimi = re.search(r'"name": "(.*?), (\d+)%vol, (\d+)ml"', nimerida)
            hinnasumma = re.search(r'"price": (\d+\.?\d*)', hinnarida)
            print(jooginimi)
            if jooginimi and hinnasumma:
                nimi = jooginimi.group(1)
                etanool = float(jooginimi.group(2))
                kogus = float(jooginimi.group(3))
                hind = float(hinnasumma.group(1))
                
                joogid.append({
                    "nimi": nimi,
                    "etanool": etanool,
                    "kogus": kogus,
                    "hind": hind
                    })
    return joogid
            
       # reader = csv.DictReader(file)
       # for row in rider
        #    joogid.append({
           #     "nimi" : row["nimi"],
           #     "etanool" : float(row["etanool"]),
            #    "hind" : float(row["hind"]),
            #    "kogus" : float(row["kogus"])
            #    })
         #   return joogid


min_etanool = float(input("sisesta enda minimaalne etanooli soovitud kogus (%): "))
max_etanool = float(input("sisesta enda maksimaalne etanooli soovitud kogus (%): "))
min_kogus = float(input("sisesta enda minimaalne joogi suurus (ml): "))
max_kogus = float(input("sisesta enda maksimaalne joogi suurus (ml): "))
min_hind = float(input("sisesta enda minimaalne hind (€): "))
max_hind = float(input("sisesta enda maksimaalne hind (€): "))
    
            
def parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind):
    sobiv_jook = []
    
    for jook in joogid:
        if (min_etanool <= jook["etanool"] <= max_etanool and
            min_kogus <= jook["kogus"] <= max_kogus and
            min_hind <= jook["hind"] <= max_hind):
            sobiv_jook.append(jook)
    return sobiv_jook
            
def etanooli_arvutus_kogus(jook):
    etanooli_ml = (jook["etanool"] / 100) * jook["kogus"]
    return etanooli_ml

def etanooli_arvutus_hind(jook):
    etanooli_ml = etanooli_arvutus_kogus(jook)
    etanooli_hind_ml_suhtes = jook["hind"] / etanooli_ml
    return etanooli_hind_ml_suhtes

if __name__ == "__main__":
    
    joogid = loeb_failist("Olud.txt")
    min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind
    sobiv_jook = parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind)
    
    if sobiv_jook:
        print("sobib jook: ")
        for jook in sobiv_jook:
            etanooli_hind = etanooli_arvutus_hind(jook)
            print(f"Nimi: {jook['nimi']}, hind: {jook['hind']} €, Etanool: {jook['etanool']} %, Kogus: {jook['kogus']} ml")
            print(f"Etanooli hind (1ml kohta): {etanooli_hind:.4f} €")
    else:
        print("Ei leidnud teile sobivat jooki")
    -----------------------

import re

def loeb_failist(failinimi):
    joogid = []
    with open(failinimi, "r" , encoding="UTF-8") as fail:
        fail.readline()
        while True:
            nimerida = fail.readline().strip()
            print("nimerida", nimerida)
            osad = nimerida.split(" ")
            print("osad", osad)
            #if osad == "purk":
               # print(osad[-2])
            if not nimerida:
                break
            hinnarida = fail.readline().strip()
            print("hinnarida", hinnarida)
            jooginimi = re.search(r'"name": "(.*?)(\s\d+,\d+%vol)\s(\d+(?:,\d+)?)L.*"', nimerida)
            hinnasumma = re.search(r'"price": (\d+\.?\d*)', hinnarida)
            print("jooginimi", jooginimi)
            if jooginimi and hinnasumma:
                nimi = jooginimi.group(1)
                etanool = float(jooginimi.group(2))
                kogus = float(jooginimi.group(3))
                hind = float(hinnasumma.group(1))
                
                joogid.append({
                    "nimi": nimi,
                    "etanool": etanool,
                    "kogus": kogus,
                    "hind": hind
                    })
    return joogid
            
       # reader = csv.DictReader(file)
       # for row in rider
        #    joogid.append({
           #     "nimi" : row["nimi"],
           #     "etanool" : float(row["etanool"]),
            #    "hind" : float(row["hind"]),
            #    "kogus" : float(row["kogus"])
            #    })
         #   return joogid


min_etanool = float(input("sisesta enda minimaalne etanooli soovitud kogus (%): "))
max_etanool = float(input("sisesta enda maksimaalne etanooli soovitud kogus (%): "))
min_kogus = float(input("sisesta enda minimaalne joogi suurus (L): "))
max_kogus = float(input("sisesta enda maksimaalne joogi suurus (L): "))
min_hind = float(input("sisesta enda minimaalne hind (€): "))
max_hind = float(input("sisesta enda maksimaalne hind (€): "))
    
            
def parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind):
    sobiv_jook = []
    
    for jook in joogid:
        if (min_etanool <= jook["etanool"] <= max_etanool and
            min_kogus <= jook["kogus"] <= max_kogus and
            min_hind <= jook["hind"] <= max_hind):
            sobiv_jook.append(jook)
    return sobiv_jook
            
def etanooli_arvutus_kogus(jook):
    etanooli_ml = (jook["etanool"] / 100) * jook["kogus"]
    return etanooli_ml

def etanooli_arvutus_hind(jook):
    etanooli_ml = etanooli_arvutus_kogus(jook)
    etanooli_hind_ml_suhtes = jook["hind"] / etanooli_ml
    return etanooli_hind_ml_suhtes

if __name__ == "__main__":
    
    joogid = loeb_failist("Olud.txt")
    min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind
    sobiv_jook = parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind)
    
    if sobiv_jook:
            print("sobib jook: ")
            for jook in sobiv_jook:
                etanooli_hind = etanooli_arvutus_hind(jook)
                print(f"Nimi: {jook['nimi']}, hind: {jook['hind']} €, Etanool: {jook['etanool']} %, Kogus: {jook['kogus']} ml")
                print(f"Etanooli hind (1ml kohta): {etanooli_hind:.4f} €")
    else:
        print("Ei leidnud teile sobivat jooki")
    






