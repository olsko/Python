
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

n = 1
while n != 10000:
    if is_perfect(n):
        print(f"{n} jest liczbą doskonałą \n")

    n +=1 