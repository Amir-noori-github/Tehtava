# Kysy  suorakulmion kanta ja korkeus
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Laske suorakulmion pinta-ala
pinta_ala = kanta * korkeus

# Laske suorakulmion piiri
piiri = 2 * (kanta + korkeus)

# Tulosta suorakulmion pinta-ala ja piiri
print(f"Suorakulmion, jonka kanta on {kanta} ja korkeus {korkeus}, pinta-ala on: {pinta_ala:.2f}")
print(f"Suorakulmion piiri on: {piiri:.2f}")
