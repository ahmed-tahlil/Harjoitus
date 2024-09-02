'''
nimi1 = "Nimi1"
nimi2 = "Nimi2"
nimi3 = "Nimi3"
age1 = 4
age2 = 8
age3 = 24

print(f"Hei {nimi1} ja ikäsi on {age1} vuotta.")
print(f"Hei {nimi2} ja ikäsi on {age2} vuotta.")
print(f"Hei {nimi3} ja ikäsi on {age3} vuotta.")

print('.........................')

names = ["Nimi1", "Nimi2", "Nimi3", "Nimi4", "Nimi5"]
ages = [age1, age2, age3, 27, 31]
##names = [nimi1, nimi2, nimi3]
print(names)
print(ages)

#listan pituus voidaan tarkistaa len() funktiolla
length = len(names)
print("Listan pituus on:", length)

# Alkioon viitataan indeksinumerolla.
print(names[3])

print(f"Hei {names[4]} ikäsi on {ages[4]} vuotta.")

#Viittaus listan ulkopuolelle tuottaa virheen
#print names[8]

#Listan läpikäynti while silmukan avulla

iterator = 0
# while 0 < 5:

while iterator < len(names):
    print(f"Hei {names[iterator]} ikäsi on {ages[iterator]}.")
    #iterator = iterator + 1
    iterator += 1

lista = ["Ville", "Liisa", "Ulla", "Anna", "Matti", "Ahmed", "Neo", "Viivi"]
print(lista[2:5])
# 2, 3 , 4 (ei viimeistä alkiota) 3 alkiota indeksistä 2 alkaen
print(lista[2:]) # kaikki loputkin alkiot indeksillä 2 alkaen
print(lista[-1]) # listan viimeinen alkio

lista1 = ["Ulla", "Matti", "Ilkka"]
yhdistetty_lista = [23, 45, 66, 67, 67, lista1]
print(yhdistetty_lista)
print(yhdistetty_lista[5][0])
'''
print("\n -------------")
print("LISTAOPERAATIOT")
'''
nimet = []
nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi != "":
    nimet.append(nimi)
    print("Anna seuraava nimi tai lopeta painamalla Enter.")
    print(nimet)
'''
lista = ["Ville", "Liisa", "Ulla", "Anna", "Matti", "Ahmed", "Neo", "Viivi"]
'''
lista.append("Uusi nimi") # uusi alkio listan loppuun
print(lista)

print(lista)
if "Ulla" in lista:
    print("Ulla löytyi listasta!")
    lista.remove("Ulla") # Poistetaan alkio, mikäli se löytyy, muuten virhe
    print(lista)
    lista.insert(0, "Ulla")
    print(lista)

    #monentenako lisätty nimi nyt oikein on
    print(lista.index("Matti"))

lisaa_nimia = ["Ines", "Aku", "Tupu", "Hupu"]
lista.extend(lisaa_nimia)
    # uusi_lista = lista + lisaa_nimia
print(lista)

lista[2] = "Lisa"
print(lista)
uusi_lista = lista.sort()
print(uusi_lista)
numero_lista = [1000, 2, ]
'''

print("Listan äpikäynti for-toistorakenteen avulla.")

for kirjain in "abcde":
    print(kirjain)

for alkio in [1,2,3,4,5]:
    print(alkio)

for nimi in lista:
    print(nimi)

#for numero in range(5, 50):
    #print(numero)

#for i in range(999, 0, -3):
    #print(i)
# käytetään edellä olevia iteroimaan nimilistaa läpi
# for silmukka iteraattorilla

print(lista)
for i in range(5): # 0, 1, 2, 3, 4, 5
    print(i)
    print(f"Terve: {lista[i]}")
listan_pituus = len(lista)
#for i in range(len(lista)):
for i in range(len(lista)): #listan pituus maksimina
    print(f"Terve: {lista[i]}")
