pi = 3.14

def odd_or_even(num):
    try:
        if int(num) % 2 == 0:
            return "even"
        else:
            return "odd"
    except (TypeError, ValueError):
        return "Not an integer."