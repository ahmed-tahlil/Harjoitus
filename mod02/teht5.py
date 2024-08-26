#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

#ensin selvitetään kuinka paljon meillä on nauloja

naulatlkm = leiviskat * 20 + naulat

# sitten selvitetään kuinka paljon meillä on luoteja yhteensä

luotilkm = naulatlkm * 32 + luodit


# nyt kun tiedämme määrän niin lasketaan massa ensin grammoina
grammat = luotilkm * 13.3

print(grammat)
# Lisäksi on olemassa jakojäännösoperaatio (%), pelkän kokonaisosan palauttava jakolasku (//)
kg = int(grammat // 1000)
gr = grammat % 1000
print(f"Massa kilogrammojen mukaan {kg} ja {gr:.2f} grammaa." )
print("Massa kilogrammojen mukaan", kg , "ja ", gr, "grammaa.")
