
while 1:
    
    word = input("Podaj słowo, sprawdzić czy jest palindromem: ")

    obrocona = ""
    for znak in word:
        obrocona = znak + obrocona

    if obrocona == word :
        print("Słowo jest palindromem")
    else:
        print("Słowo nie jest palindromem")