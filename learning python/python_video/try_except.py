try:
    number = float(input("Enter a number: "))
    value = 10 / 0
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input.")