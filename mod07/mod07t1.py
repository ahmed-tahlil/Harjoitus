#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.



def vuodenajat(kuukausi):
   vuodenajat = {"Talvi": (12,1,2), "Kevät": (3,4,5), "Kesä": (6,7,8), "Syksy":(9,10,11)
    }
   for vuodenaika, kuukaudet in vuodenajat.items():
        if kuukausi in kuukaudet:
            return vuodenaika


kuukausi = int(input("Anna kuukauden numero: "))

#vuodenajat(kuukausi)

if kuukausi < 1 or kuukausi > 12:
    print("Virheellinen valinta.")

else:
    vuodenaika = vuodenajat(kuukausi)
    print(f"Valitsemasi kuukauden vuodenaika on {vuodenaika}. ")
