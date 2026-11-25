ciag = input("Wpisz tekst: ")
litery = {
}

for char in ciag:
    char = char.lower()
    if char.isalpha():
        if char in litery:
            litery[char] += 1
        else:
            litery[char] = 1



ilosc_liter = len(litery)

if len(litery) != 0:

    naj_litera = max(litery, key=litery.get)
    print(f"Liczba różnych liter: {ilosc_liter}")
    print(f"Najczęściej występująca litera: {naj_litera}, która występuje {litery[naj_litera]}.")

else:
    print("Tekst jest pusty")

