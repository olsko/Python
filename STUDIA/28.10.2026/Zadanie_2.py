import math
print("Równanie kwadratowe")

a = int(input("Liczba a wynosi: "))
b = int(input("Liczba b wynosi: "))
c = int(input("Liczba c wynosi: "))

print("\n")

if a == 0:
    print("Funkcja nie jest kwadratowa")
else:

    our_delta = b ** 2 - 4 * a * c # obliczenie delty

    if our_delta < 0 :
        print("Nie ma rozwiązań dla x w grupie liczb rzeczywistych")

    elif our_delta == 0 :
        x_one = (-b) / (2*a)

        print(f"Delta równa się: \n{our_delta} \ni jest jedno rozwiązanie\nx = {x_one}")

    elif our_delta > 0 :
        x_one = (-b - math.sqrt(our_delta)) / (2 * a)
        x_two = (-b + math.sqrt(our_delta)) / (2 * a)
        
        print(f"Delta równa się: \n{our_delta} \ni są dwa rozwiązania\nx_1 = {x_one}\nx_2 = {x_two}")


