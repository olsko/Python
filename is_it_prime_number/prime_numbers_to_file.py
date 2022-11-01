def prime_check(num):
    divisible = []
    for i in range(11):
        if i > 0 and num % i == 0 :
            divisible.append(i)
    
    if len(divisible) > 2:
        return " isn't prime."
    else:
        return " is prime."

prime_list = open("prime_list.txt", "a")

print("How many numbers to test if they are prime?")
count = 0
for i in range(int(input(": "))):
    count += 1
    result = prime_check(i)
    prime_list.write("\n" + str(count) + ". " + "The number " + str(i) + result)
    