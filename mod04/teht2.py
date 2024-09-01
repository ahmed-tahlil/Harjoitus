tuuma = input("Kerro tuumien määrä: ")
tuuma = int(tuuma)
while tuuma >= 0:
    sentti = tuuma * 2.54
    print(f"Antamasi tuumat {tuuma} ovat {sentti} senttimetriä.")
    tuuma = int(input("Kerro tuumien määrä: "))
    if tuuma < 0:
        break
