import math
import random
#Ex1
# Kirjoita ohjelma, joka kysyy nimesi ja sen jälkeen tervehtii sinua omalla nimelläsi. Esimerkkejä:
# Jos syötät nimeksesi Viivi, ohjelma tervehtii sinua sanoin Terve, Viivi!
# Jos syötät nimeksesi Ahmed, ohjelma tervehtii sinua sanoin Terve, Ahmed!

username = input("Anna nimesi: ")
print("Terve, " + username)

# Ex2
# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

R = input("Radius: ")
A = math.pi * float(R) * float(R)

print(f"The area of a circle: {A:.2f}")

# Ex3
# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. 
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

a = float(input("length "))
b = float(input("width "))

P = str(2 * a + 2 * b)
S = str(a * b)

print("Perimeter is: " + P)
print("Area is: " + S)

# Ex4
# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
num_3 = float(input("Enter third number: "))

summa = str(num_1 + num_2 + num_3)
product = str(num_1 * num_2 * num_3)
average = str((num_1 + num_2 + num_3)/3)

print("Summa: " + summa)
print("Product: " + product)
print(f"Avrage: {average:.2f})

# Ex5
# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))



modern_units = ((((talents * 20) + pounds) * 32) + lots) * 13.3

kg = modern_units // 1000
g = modern_units % 1000
print(f"Weight in modern units: {kg:.2f}kg and {g:.2f}g.")

# Ex6
# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
# Vihje: tutustu random.randint()-funktion käyttöön.

import random

code3 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
code4 = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))

print("Kolmenumeroisen koodin:", code3)
print("Nelinumeroisen koodi:", code4)