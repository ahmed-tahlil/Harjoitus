pituus = float(input("Mikä on kuhan pituus senttimetreinä? "))
if pituus < 37:
    erotus = 37 - pituus
    print(f"Laske kuha takaisin järveen. Sinulta puuttuu pyyntimitasta {erotus:.0f} senttimetriä.")
