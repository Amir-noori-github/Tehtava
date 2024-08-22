import random

# Arvo kolmenumeroinen koodi, jossa jokainen numero on väliltä 0..9
kolmenumeroinen_koodi = ''.join(str(random.randint(0, 9)) for _ in range(3))

# Arvo nelinumeroinen koodi, jossa jokainen numero on väliltä 1..6
nelinumeroinen_koodi = ''.join(str(random.randint(1, 6)) for _ in range(4))

# Tulosta arvotut koodit
print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumeroinen_koodi}")


