#def alkoholikogus(kogus_ml, %):
    #return (kogus_ml * protsent) / 100:

#def alkoholi_hinna_suhe(alkoholikogus_joogis, hind):
    #return alkoholikogus_joogis / hind

#failinimi = "õlud.txt"

#try:
     #fail = open("õlu.txt", encoding="UTF-8")
        #for rida in fail:
           # rida = rida.strip()
            #read = rida.split(",")
            
def parimjoogivalik(min_etanool, max_etanool, min_kogus, max_kogus, min_hind, max_hind, failinimi):
    sobiv_jook = none
    
    filtreeritud = (
        ["etanool_protsent"] >= min_etanool
        ["etanool_protsent"] <= max_etanool
        ["maht_ml"] >= min_maht * 1000
        ["maht_ml"] <= max_maht * 1000
        ["hind_eurodes"] >= mix_hind
        ["hind_eurodes"] <= max_hind
        )
    
    valib_sobiva_joogi = [filtreeritud]
    
    if valib_sobiva_joogi.empty:
        return "Sellist jooki pole"
    
    Sobivjook = valib_sobiva_joogi.sort_values(by="hind")
    return Sobivjook

min_etanool = float(input("sisesta enda minimaalne etanooli soovitud kogus: "))
max_etanool = float(input("sisesta enda maksimaalne etanooli soovitud kogus: "))
min_kogus = float(input("sisesta enda minimaalne joogi suurus: "))
max_kogus = float(input("sisesta enda maksimaalne joogi suurus: "))
max_hind = float(input("sisesta enda maksimaalne hind: "))
min_hind = float(input("sisesta enda minimaalne hind: "))
        

