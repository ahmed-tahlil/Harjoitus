# alustus ehtolauseille
'''
rahat = float(input("Anna rahamääräsi: "))

if rahat >= 5:
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa")
print("Jatketaan pääohjelmaa")

#Sama kuin

rahat = float(input("Anna rahamääräsi: "))
ehto = (rahat >= 5)
print(ehto)

if ehto:
    #tämä osa on lohko ja suoritetaan jos ehto on totta
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa")
print("Jatketaan pääohjelmaa")
'''

## Luo ohjelma joka pyytää käyttäjän numeron ja tulostaa onko luku pos, neg vai nolla
'''
num = int(input("Anna numero: "))
if num > 0:
    print("Luku on positiivinen.")
if num < 0:
    print("Luku on negatiivinen")
if num == 0:
            print("Luku on nolla")
'''
#kaksi toisensa poissulkevaa vaihtoehtoa
'''
rahat = float(input("Anna rahamäärä: "))
if rahat>=5:
    print("Voit ostaa latten.")
else:
    print("Sinulla ei valitettavasti ole tarpeeksi rahaa latteen")
    '''

# monta vaihtoehtoa

user_input = input("Valite a, b, tai c ")
if user_input == "a":
    print("Tehdään jotain, käyttäjä valitsi kirjaimen a")
elif user_input == "b":
    print("Tehdään jotain muuta kivaa, käyttäjä valitsi kirjaimen b")
elif user_input == "c":

 #lohkossa on usein paljonkin koodia ja kaikki sisennetty suoritetaan

    print("Käyttäjä valitsi")
    print("Moikka saat c luokan hytin")
    a = 4 + 4
    print(f"Saat rahaa buffaan {a}euroa bonuksena")
else:
    print("Käyttäjä ei syöttänyt a, b, tai c. Ei tehdä siis mitään")

print("Ohjelma loppuu, hei hei")