sp = input("Kerro sukupuolesi?")
hglo = int(input("Kerro hemoglobiiniarvo (g/l)?"))
if sp == "Mies" and 134 <= hglo <= 195:
    print("Hemoglobiiniarvosi on normaali.")
elif sp == "Mies" and hglo < 134:
    print("Hemoglobiiniarvosi on matala.")
elif sp == "Mies" and hglo > 195:
    print("Hemoglobiiniarvosi on korkea.")
elif sp == "Nainen" and 117 <= hglo <= 175:
    print("Hemoglobiiniarvosi on normaali.")
elif sp == "Nainen" and hglo < 117:
    print("Hemoglobiiniarvosi on matala.")
elif sp == "Nainen" and hglo > 175:
    print("Hemoglobiiniarvosi on korkea.")