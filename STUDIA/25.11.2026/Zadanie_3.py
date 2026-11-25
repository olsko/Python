common_passwords = ["password", "qwert12", "12345678", "admin123"]

password_user = input("Podaj hasło: ")

good_password = 1

if len(password_user) < 8 :
    print("Hasło jest za krótkie (8 znaków)")
    good_password = 0

for i in range(len(common_passwords)) :
    if common_passwords[i] == password_user:
        print("Hasło jest za często używane")
        good_password = 0
        break

if   " " in password_user:
    print("Hasło nie powinno mieć w sobie spacji")
    good_password = 0

if good_password :
    print("Hasło jest w porządku do użycia")
else:
    print("Hasło jest do poprawy")