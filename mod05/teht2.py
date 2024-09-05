#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

user_input = input("Anna kokonaisluku? ")
kokonaisluvut = []
while user_input != "":
    kluku = int(user_input)
    kokonaisluvut.append(kluku)
    kokonaisluvut.sort(reverse = True)
    print(kokonaisluvut)
    user_input = input("Anna kokonaisluku?")
print(kokonaisluvut[:5])



