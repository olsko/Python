a = 6048
b = 6720

def divisors(n):

    divisions = set()

    for i in range(1, n+1):
        if n % i == 0:
            print(i)
            divisions.add(i)
    return(divisions)


divisors_a = divisors(a)
divisors_b = divisors(b)


print(f"Liczba wspólnych dzielników: {len(divisors_a & divisors_b)}")

print(f"Największy wspólny dzielnik: {max(divisors_a & divisors_b)}")

print(f"Liczba dzielników tylko w zbiorze A: {len(divisors_a - divisors_b)}")


print(f"Liczba dzielników tylko w zbiorze B: {len(divisors_b - divisors_a)}")
