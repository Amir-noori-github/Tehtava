# Kysy kolme kokonaislukua
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

# Laske lukujen summa
summa = luku1 + luku2 + luku3

# Laske lukujen tulo
tulo = luku1 * luku2 * luku3

# Laske lukujen keskiarvo
keskiarvo = summa / 3

# Tulosta lukujen summa, tulo ja keskiarvo
print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo:.2f}")

