distance = float(input( "Wprowadź odległość w kilometrach: "))
fuel_avg = float(input( "Wprowadź średnie zużycie paliwa (l/100km): "))
fuel_price = float(input( "Wprowadź cenę paliwa (zł/l): "))
number_of_passengers = int(input( "Wprowadź liczbę pasażerów: "))


fuel_needed = (distance / 100) * fuel_avg
price_needed = fuel_needed * fuel_price
price_per_passenger = price_needed / number_of_passengers



print(f"\n\nIlość paliwa potrzebna do pokonania trasy: {fuel_needed:.2f}\nCałkowity koszt paliwa: {price_needed:.2f}\nKoszt na osobę: {price_per_passenger:.2f}")