# MONIKKO
################################################

print("\nMonikko ()\n")

# Monikko (tuple) on "kuin lista jota ei voi muokata"

minun_lista = [1,2,3,4,5,6]
print(minun_lista)

minun_monikko = (1,2,3,4,5,6)
#minun_monikko = 1,2,3,4,5,6
print(minun_monikko)

minun_monikko2 = (1,2,(3,4), 5, "kuusi")
print(minun_monikko2)

# luetaan ensimmäinen alkio
print(minun_lista[0])
print(minun_monikko[0])

# yritetään nyt muokata eka alkio numeroksi 0 ja lisätä loppuun 7
# listan sisältöä voi muokata, mutable
minun_lista[0] = 0
minun_lista.append(7)
print(f"Muokattu lista {minun_lista}")

# monikon sisältöä EI voi muokata, immutable
#minun_monikko[0] = 0

# Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on luonteeltaan staattinen:
# Tiedetään että muutoksille ei ole tarvetta ohjelman suorituksen aikana.
''''
#Koodiesimerkki materiaalista
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
print(viikonpäivät[järjestysnumero-1])
print(f"{järjestysnumero}, viikonpäivä on {viikonpäivä}.")
'''
''''
# Monikon läpikäynti kuten listan
minun_monikko3 = ("eka", "toka", "kolmas", "neljäs")
for i in minun_monikko3:
    print(i)

  ##  if i == "kolmas":
 ###       print("kolmas löytyi")
        break
'''
#Monikon arvojen purku muuttujiin

hedelmät = ("Lime", "Sitruuna", "Appelsiini")
# (eka,toka, kolmas) = ("Lime", "Sitruuna", "Appelsiini")
(eka, toka, kolmas) = hedelmät
print(eka)
sanalista = ("eka", "toka", "kolmas", "neljäs","viides")

print("Terve!")
def tulosta_monikko(sanalista):
    for i in sanalista:
        print(i)

tulosta_monikko(sanalista)
tulosta_monikko(hedelmät)

#Monikko funktion paluuarvona

import random



def heitä():
    eka,toka = random.randint(1,6), random.randint(1, 6)
    print(f"Nopista tuli {eka} ja {toka}.")

heitä()

#Monikko funktion paluuarvona


def heitä2():
    (eka,toka)= random.randint(1,6), random.randint(1, 6)

    return (eka,toka)

noppa1, noppa2 = heitä2()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

#JOUKKO eli set {}

# JOUKKO (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.

#kOSKA JOUKON alkioille ei ole määriteltyä järjestystä, ei alkioihin voi myöskään viitata indeksillä

# Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen, eli joukossa ei voi olla kahta samansisältöistä alkiota.


#joukko eli set

joukko = {1,2,3,4,5,6}
# joukko merkataan aaltosulkeilla

print(joukko)

print(f"Nupmero 6 voi esiintyä listassa useasti:")
minun_lista = [6,2,3,4,5,6]
print(minun_lista)

print(f"Nupmero 6 voi esiintyä monikossa useasti:")
minun_monikko = [6,2,3,4,5,6]
print(minun_lista)

print(f"Nupmero 6 EI voi esiintyä monikossa useasti:")
minun_joukko = {6,2,3,4,5,6}
print(minun_joukko)

# yllä oleva ei sinänsä tuota virhettä, kuten ei add-metodi

minun_joukko.add(6) # ei onnistu, mutta ei tuota virhettä
minun_joukko.add(7)
print(minun_joukko)
minun_joukko.remove(7)
print(minun_joukko)

#koodiesimerkki, järjestys voi muuutua printatessa

pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("DOminion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

# alkiot iteroidaan läpi for/in rakenteella

for p in pelit:
    print(p)
    # löytyykö Cluedo, jos löytyy printtaa jotain

    if p == "Cluedo":
        print("Cluedo löytyi!!!½!!!")
# if/in haku toimii kuten listoissa
if "Monopoli" in pelit:
     print("Monipoli löytyi!!!!!")

# tyhjä joukko luodaan edellä esitetystä poiketen set-funktion avulla.

autolista = []
autolista.append("Audi")
print(autolista)
# tästä tuleekin sanakirja eli dictionary
autojoukko = {}
print(type(autojoukko))

# Tyhjä joukku luodaan edellä esitetystä poiketen set-funktion avulla.
autojoukko = set()
autojoukko.add("Audi")
print(type(autojoukko))  # tämä on <class 'set'>
print(autojoukko)


#############################################################

# SANAKIRJA {}

#######################################################################


print("\n SANAKIRJA {}  \n")

#Sanakirja (dictionary) on Pythonin käytetyimpiä tietorakenteita.
#Sanakirjaan voidaan tallentaa avain-arvopareja.

#Kun sanakirja alustetaan arvot luettelemalla, annetaan kukin avain-arvopari seuraavasti: avain : arvo. Peräkkäiset avain-arvoparit erotellaan toisistaan pilkulla.

oppilaat = {"Aapeli": 25, "Bertta": 45, "Cecilia": 11, "Daniel": 3, "Emma": 22}
print(oppilaat)

# mitä ovat tietueet / items
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa?
print(oppilaat.keys())

#mitä ovat arvoja sanakirjassa
print(oppilaat.values())

# kun sanakirjaa käydään läpi for/in rakenteella:

# tietueet eli avain-arvoparit

for i in oppilaat.items():
    print(i)


# Kun sanakirja läpikäydään for/in-rakennetta käyttäen, saa kierrosmuuttuja arvokseen vuoron perään kunkin sanakirjassa esiintyvän avaimen.
for i in oppilaat:
    print(i)

print(oppilaat["Aapeli"])

#arvot
for i in oppilaat:
    print(i)

avain = "Aapeli"
print(oppilaat["Aapeli"])
print(oppilaat[avain]) # etsii avaimella Aapeli sen arvoa joka on 25

# etsi kaikki arvot

for i in oppilaat:
    print(oppilaat[i])
''''
# if / in rakenteella voidaan myös hakea sanakirjasta tietoa

nimi = input("Anna nimi, niin etsin sen sanakirjasta jos löytyy: ")

if nimi in oppilaat:
    print(f"Oppilas löytyi {nimi} ja ikää hänellä {oppilaat[nimi]}")
'''
# Kun olemassa olevaan sanakirjaan lisätään arvo,
# käytetään notaatiota sanakirja[avain] = arvo
#lisätään uusi oppilas mikäli ei löydy
#jos avain löytyy, se muokkaa olemassa olevaa, joten luodaan uusi

oppilaat["Ulla"] = 22
print(oppilaat)