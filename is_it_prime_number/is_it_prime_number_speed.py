import timeit
from random import randint
from decimal import *
def prime_check(num):
    divisible = []
    for i in range(11):
        if i > 0 and num % i == 0 :
            divisible.append(i)
    
    if len(divisible) > 2:
        return " isn't prime."
    else:
        return " is prime."

results = []
for i in range(10000):
    input = randint(0,100000000000000000000000000000000000)
    start_time = timeit.default_timer()
    print(prime_check(input))
    results.append("%s" % (timeit.default_timer() - start_time))
    print("--- It took %s seconds ---" % (timeit.default_timer() - start_time))

print(results)
print(len(results))

sum = Decimal("0")
for i in results:
    num = Decimal(i)
    sum += num
average = Decimal(0)
average = sum / len(results)
print(average)