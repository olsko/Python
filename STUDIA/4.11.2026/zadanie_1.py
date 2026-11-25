word = list(input("Podaj słowo, sprawdzić czy jest palindromem: "))


if word == word[::-1]:
    print("Słowo jest palindromem")
else:
    print(f"Słowo nie jest palindromem\n {word}, {word[::-1]}")