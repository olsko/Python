from random import randint
from sympy import isprime
import timeit
from decimal import *
getcontext().prec = 999 #decimal precision
results = []
for i in range(10000):
    input = randint(0,100000000000000000000000000000000000)
    start_time = timeit.default_timer()
    print(isprime(input))
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