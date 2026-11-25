
for number in range (1000):
    result = 0
    i = 0
    for i in range(number):
        i += 1
        if number % i == 0:
            result += 1


    if result == 2:
        print(number)