int1 = input("Kerro ensimmäinen kokonaisluku?")
int2 = input("Kerro toinen kokonaisluku?")
int3 = input("Kerro kolmas kokonaisluku?")

summa = int(int1) + int(int2) + int(int3)
tulo = int(int1) * int(int2) * int(int3)
ka = int(summa / 3)

print("Lukujen summa on " + str(summa))
print("Lukujen tulo on " + str(tulo))
print("Lukujen keskiarvo on " + str(ka))