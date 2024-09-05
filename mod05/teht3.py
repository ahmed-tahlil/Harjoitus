# funktio alkuluvun määrittelyyn

def onko_alkuluku(num):
    # jätetään nolla ja negatiiviset luvut kokonaan testaamatta
    if num < 1:
        return False
    tulos = True
    for i in range(2, num):

        #print(i)
        if num % i == 0:
            # jos jaollinen jollain i:n arvolla, palautetaan false
            # ja funktion suoritus loppuu siihen
            return False
    # jos funktion suoritus on jatkunut tänne asti, niin palautetaan tänne asti

    return True
# pääohjelma joka lukee syötteen ja tulostaa vastauksen

user_input = int(input("Anna testattava luku (>0): "))

if onko_alkuluku(user_input):
    print(f"Luku {user_input} on alkuluku.")
else:
    print(f"Luku {user_input} ei ole alkuluku")






#funktion toimintaa erilaisilla arvoilla
#print(onko_alkuluku(4))
#print(onko_alkuluku(280))
#print(onko_alkuluku(0))