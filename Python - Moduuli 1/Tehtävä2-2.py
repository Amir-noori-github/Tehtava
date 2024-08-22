import math

# Kysy ympyrän säde
sade = float(input("Anna ympyrän säde: "))

# Laske ympyrän pinta-ala
pinta_ala = math.pi * (sade ** 2)

# Tulosta ympyrän pinta-ala
print(f"Ympyrän, jonka säde on {sade}, pinta-ala on: {pinta_ala:.2f}")
