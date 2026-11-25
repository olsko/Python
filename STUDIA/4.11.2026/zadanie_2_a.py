a = int(input("Podaj dodatnią liczbę całkowitą: "))
b = 0
ciag = [a]

#Jeśli parzysta
while a != 1:
    
    b = a

    if a % 2 == 0 :
            a = a/2
    else:
            a = 3*a +1

    ciag.append(a)

print(ciag)
print(len(ciag))
