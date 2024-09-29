def highlow():
    import random

    # korttipakan luonti

    maat = ["Hertta", "Pata", "Risti", "Ruutu"]

    numerot = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    korttipakka = [(numero, maa) for maa in maat for numero in numerot]

    # Muunna korttien arvot numeroksi vertailua varten
    korttiarvot = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def valikko():
        print("Tervetuloa pelaamaan Higher or Lower -korttipeliä!")
        print("Paina 'p' aloittaaksesi pelin")
        print("Paina 'o' saadaksesi peliohjeet")
        print("Paina 'q' lopettaaksesi pelin")

    def ohjeet():
        print("\nPELIN OHJEET:\n")
        print("1. Pelissä on 5 kierrosta.")
        print("2. Sinulle näytetään pelikortteja ja sinun pitää arvata onko seuraava pelikortti 'k' korkeampi vai 'p' pienempi.")
        print("3. Saat yhden pisteen oikeasta arvauksesta.")
        print("4. Voit lopettaa pelin milloin tahansa painamalla 'q'.\n")


    # pelin funktio

    def peli_hl():
        ### pelin toiminnot
        random.shuffle(korttipakka)
        pisteet = 0
        loss = 0
        kiekat = 5

        for kiekka in range(kiekat):
            # ottaa kortin pakasta
            if len(korttipakka) == 0:
                print("Korttipakka loppui!")
                break

            ensimmainen_kortti = korttipakka.pop()

            print(f"\nKierros {kiekka + 1}/{kiekat}")
            print(f"Ensimmäinen kortti: {ensimmainen_kortti[0]}, {ensimmainen_kortti[1]}")
            arvaus = input("Onko seuraava kortti 'k' (korkeampi)  vai 'p' (pienempi)? tai ('q' jos haluat lopettaa).").lower()

        ## pelin lopetus
            if arvaus == 'q':
                print("Peli lopetettu.")
                break

            while arvaus not in ['k', 'p', 'q']:
                print("Virheellinen valinta! Valitse 'k' (korkeampi) tai 'p' (pienempi)? (tai 'q' jos haluat lopettaa.)")
                arvaus = input("Onko seuraava kortti 'k' (korkeampi)  vai 'p' (pienempi)? (tai 'q' jos haluat lopettaa.)").lower()

    # ottaa seuraavan kortin pakasta
            seuraava_kortti = korttipakka.pop()
            print("Seuraava kortti: ", seuraava_kortti[0], seuraava_kortti[1])

                #korttien vertailu
            ekan_arvo = korttiarvot[ensimmainen_kortti[0]]
            tokan_arvo = korttiarvot[seuraava_kortti[0]]

            if arvaus == "k" and tokan_arvo > ekan_arvo:
                print("Oikein! Sait yhden pisteen.")
                pisteet += 1
            elif arvaus == "p" and ekan_arvo > tokan_arvo:
                print("Oikein! Sait yhden pisteen.")
                pisteet += 1
            else:
                print("Väärin! Hävisit kierroksen.")
                loss += 1

            if loss == 3:
                print("Hävisit pelin.")
                break

        print(f"\nPeli päättyi! Voitit {pisteet} kierrosta.")
        if pisteet >= 3:
            print("Voitit pelin!")
        else:
            print("Hävisit pelin.")




    while True:
        valikko()
        valinta = input("Valintasi: ").lower()

        if valinta =='p':
            peli_hl()
        elif valinta =='o':
            ohjeet()
        elif valinta =='q':
            print("Peli lopetettu.")
            break
        else:
            print("Virheellinen valinta! Yritä uudelleen.")

    








