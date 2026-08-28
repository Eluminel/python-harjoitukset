# #Ex1
# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, 
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. 
# #Kuha on alamittainen, jos sen pituus on alle 37 cm.

pituus = float(input("Kuhan pituuden senttimetreinä: "))

if pituus < 37:
    print(f"Laskea kuhan takaisin järveen, tarvitaan {37 - pituus} senttimetriä enemmän.")
else:
    print("Ota kuha mukaasi.")

# Ex2
# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.

laivan_hyttiluokka = input("Anna laivan hyttiluokka: ").upper()

if laivan_hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif laivan_hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif laivan_hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella..")
elif laivan_hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!")

# Ex3
# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

# sukupuoli = input("Anna sukupuilisi(nainen tai mies): ").lower()
# try:
#     hemoglobiini = float(input("Anna hemoglobiiniarvo: "))
# except ValueError:
#     print("Virheelliset hemoglobiiniarvo.")

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Teillä on alhainen hemoglobiinitaso.")
    elif 117<= hemoglobiini <= 175:
        print("Teillä on normaali hemoglobiinitaso.")
    else:
        print("Teillä on korkea hemoglobiinitaso.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Teillä on alhainen hemoglobiinitaso.")
    elif 134 <= hemoglobiini <= 195:
        print("Teillä on normaali hemoglobiinitaso.")
    else:
        print("Teillä on korkea hemoglobiinitaso.")
else:
    print("Annettu sukupuoli on virheellinen.")

# Ex4
# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. 
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. 
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosi: "))

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        print("Tämä vuosi ei ole karkausvuosi.")
    else:
        print("Tämä vuosi on karkausvuosi.")
else:
    print("Tämä vuosi ei ole karkausvuosi.")