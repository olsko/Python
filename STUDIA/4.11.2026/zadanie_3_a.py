number = int(input("Podaj dodatnią liczbę całkowitą: "))
result = 0

for i in range(number):
    i += 1
    print(i)
    if number % i == 0:
        result += 1


if result == 2:
    print(f"Liczba {number} jest liczbą pierwszą")
else:print(f"Liczba {number} nie jest liczbą pierwszą")

