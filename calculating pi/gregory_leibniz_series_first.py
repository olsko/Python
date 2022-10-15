from operator import add
from operator import sub
import time
from decimal import *
getcontext().prec = 999 #decimal precision
def calculate_pi(times): 
    pi= 0
    number = Decimal("-1")
    operation  = add
    a = Decimal("0")
    for i in range(int(times)):
        if operation == add:
            operation = sub
        else:
            operation = add
        number = number + 2
        if a == 0:
            a = 4 / number
            number = number + 2
            b = Decimal("0")
            b = 4 / number
            c = Decimal("0")
            c = operation(a,b)
        else:
            a = 4 / number
            c = operation(c,a)
        pi = Decimal("0")
        pi = c
        print(str(i + 1))
    return pi
iterations = input("How many iterations: ")
start_time = time.time()
result =  str(calculate_pi(iterations))
print("\n")
print("Calculated pi: " + result)
print("--- It took %s seconds ---" % (time.time() - start_time))