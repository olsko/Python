numbers = [7, 3, 9, 2, 5, 1, 8, 4, 6]
numbers2 = numbers.copy()
liczba_przejsc = 0
zmiana = 1

while zmiana != 0:
    zmiana = 0
    for i in range(len(numbers)):
            
            if len(numbers) != i+1:

                if numbers[i] > numbers[i+1]:
                    zmiana += 1
                    numbers2[i] = numbers[i+1]
                    numbers2[i+1] = numbers[i]
                    
                    numbers = numbers2.copy()

    
    liczba_przejsc += 1

lista_posortowana = numbers2

print(f"Lista po sortowaniu {lista_posortowana}")
print(f"Liczba przejsc: {liczba_przejsc}")