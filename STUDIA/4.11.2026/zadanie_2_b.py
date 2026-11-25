dlugosc_ciagu_teraz = 1
najdluzszy_ciag = 0
rezultat = []

for i in range(1000):
        i += 1
        dlugosc_ciagu_teraz = 1
        a = i
        ciag = [a]
        while a != 1:
                if a % 2 == 0 :
                        a = a/2
                else:
                        a = 3*a +1
                dlugosc_ciagu_teraz += 1
                ciag.append(a)

        if dlugosc_ciagu_teraz > najdluzszy_ciag:
                rezultat = [dlugosc_ciagu_teraz, i]
                najdluzszy_ciag = dlugosc_ciagu_teraz

print(rezultat)