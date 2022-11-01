def prime_check(num):
    divisible = []
    for i in range(11):
        if i > 0 and num % i == 0 :
            divisible.append(i)
    
    if len(divisible) > 2:
        return " isn't prime."
    else:
        return " is prime."


print(("Imput a number to test if it is prime."))
input = int(input(": "))
result = prime_check(input)
print("The number " + str(input) + result)