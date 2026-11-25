price_ticket_standard = 40


def discount(price, age, card_ownership):
    
    discount_value = 0
    if age < 7: #za darmo dla dzieci, brak dalszych sprawdzeń
        price = 0
        return price

    #sprawdzenie wieku
    elif age >= 7 and age <= 18:

        discount_value += 50

    elif age >= 65:
        discount_value += 25

    #karta
    if card_ownership == "tak":
        discount_value += 10

    return price - (price * (discount_value / 100))



print("Obliczenie cenny biletu do muzeum")

age = int(input("Wprowadź swój wiek jako liczba: "))

card = input("Wprowadź czy masz kartę (tak lub nie): ")

final_price = discount(price_ticket_standard, age, card)

print(f"Finalna cena do zapłacenia: {final_price:.2f} zł")