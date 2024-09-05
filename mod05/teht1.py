import random
total = 0
tulos_lista = []
dice_count = int(input("Montako noppaa laitetaan?"))
for i in range(dice_count):
    tulokset = random.randint(1,6)
    total = total + tulokset
    tulos_lista.append(tulokset)
print(f"Noppien silmälukujen summa on {total}. Nopat: {tulos_lista}")

