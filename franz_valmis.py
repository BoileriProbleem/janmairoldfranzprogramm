import re

def loeb_failist(failinimi):
    joogid = []
    with open(failinimi, "r", encoding="UTF-8") as fail:
        fail.readline()  
        while True:
            nimerida = fail.readline().strip()
            if not nimerida:
                break  

            hinnarida = fail.readline().strip()

            
            jooginimi = re.search(r'"name": "(.*?)\s(\d+%)\s(\d+(?:,\d+)?)[lL]', nimerida) or re.search(r'"name": "(.*?)\s(\d+,\d+%vol)\s(\d+(?:,\d+)?)[lL]' , nimerida) or re.search(r'"name": "(.*?)\s(\d+%vol?)\s(\d+(?:,\d+)?)[lL]', nimerida)
            hinnasumma = re.search(r'"price": (\d+\.?\d*)', hinnarida)

            if jooginimi and hinnasumma:
                    nimi = jooginimi.group(1)  
                    etanool = float(jooginimi.group(2).replace(',', '.').strip('%vol').strip("%"))

                    # Check for "-pakk" and extract the quantity
                    match = re.search(r'(\d+)-pakk"', nimerida)
                    if match:
                        kogus = float(match.group(1)) * float(jooginimi.group(3).replace(',', '.'))
                    else:
                        kogus = float(jooginimi.group(3).replace(',', '.'))  

                    hind = float(hinnasumma.group(1))

                    joogid.append ({
                        "nimi": nimi,
                        "etanool": etanool,
                        "kogus": kogus,
                        "hind": hind
                    })
            else:
                print(nimerida)

    return joogid

min_etanool = float(input("Sisesta minimaalne etanooli soovitud kogus (%): "))
max_etanool = float(input("Sisesta maksimaalne etanooli soovitud kogus (%): "))
min_kogus = float(input("Sisesta minimaalne joogi suurus (L): "))
max_kogus = float(input("Sisesta maksimaalne joogi suurus (L): "))
min_hind = float(input("Sisesta minimaalne hind (€): "))
max_hind = float(input("Sisesta maksimaalne hind (€): "))


def parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind):
    parim_jook = None
    parim_hind = float('inf')  

    for jook in joogid:
        if (min_etanool <= jook["etanool"] <= max_etanool and
            min_kogus <= jook["kogus"] <= max_kogus and
            min_hind <= jook["hind"] <= max_hind):
            etanooli_hind = etanooli_arvutus_hind(jook)  

            if etanooli_hind < parim_hind:  
                parim_hind = etanooli_hind
                parim_jook = jook

    return parim_jook

def etanooli_arvutus_kogus(jook):
    etanooli_ml = (jook["etanool"] / 100) * jook["kogus"] * 1000  
    return etanooli_ml

def etanooli_arvutus_hind(jook):
    etanooli_ml = etanooli_arvutus_kogus(jook)
    etanooli_hind_ml_suhtes = jook["hind"] / etanooli_ml
    return etanooli_hind_ml_suhtes

if __name__ == "__main__":
    joogid = loeb_failist("Lahja.txt")
    parim_jook = parimjoogivalik(joogid, min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind)

    if parim_jook:
        etanooli_hind = etanooli_arvutus_hind(parim_jook)
        print(f"Leitud sobiv jook:")
        print(f"Nimi: {parim_jook['nimi']}, Hind: {parim_jook['hind']} €, Etanool: {parim_jook['etanool']} %, Kogus: {parim_jook['kogus']} L")
        print(f"Etanooli hind (1ml kohta): {etanooli_hind:.4f} €")
    else:
        print("Ei leidnud sobivat jooki.")
