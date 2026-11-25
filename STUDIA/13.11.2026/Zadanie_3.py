
def is_perfect(n):
    dzielniki = []

    for i in range(n):
            i += 1
        
            if n % i == 0 and i != n:
                dzielniki.append(i)

            
    
    suma = 0

    for i in range(len(dzielniki)):
        suma += dzielniki[i]
        i += 1

    if suma == n:
         return(True)
    else:
         return(False)



if is_perfect(int(input("Podaj możliwą liczbę całkowitą: "))):
    print("Liczba jest doskonała")

else:
    print("Liczba nie jest doskonałą")