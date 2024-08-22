# Kysy leivisköiden, naulojen ja luotien määrä
leiviskat = int(input("Anna leivisköiden määrä: "))
naulat = int(input("Anna naulojen määrä: "))
luodit = int(input("Anna luotien määrä: "))

# Muunna kaikki massa grammoiksi
grammat = (leiviskat * 20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit * 13.3)

# Muunna grammat kilogrammoiksi ja jäljelle jääviksi grammoiksi
kilogrammat = int(grammat // 1000)  # Kokonaiset kilogrammat
jäljellä_grammat = grammat % 1000  # Jäljelle jäävät grammat

# Tulosta tulos
print(f"Annettu massa on: {kilogrammat} kg ja {jäljellä_grammat:.2f} g")
