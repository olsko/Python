#Parametry
laps = 5 # razy
distance = 400 # metry
lap_times = [64.2, 62.8, 63.5, 61.9, 62.4]


#Calculate avg time
sum_laps_time = sum(lap_times)

avg_time = sum_laps_time / len(lap_times)


#Difrerence beetwen max and min

dif_max_min_speed = max(lap_times) - min(lap_times)

#Avarage speed km/h

#Zamienienie dystansu na km, a czas na godziny

avg_speed = round( ((distance * laps)/1000) / (sum_laps_time/3600), 2)
#How long to acomplish 5 km
#Ile czasu w godzinach aby 5km
time_5km = 5 / avg_speed

#Na minuty potem sekundy
minutes_5km = time_5km * 60

minutes = int(minutes_5km)

seconds = (minutes_5km - minutes) * 60

print(f"\n\nŚredni czas okrążenia: {avg_time:.2f}s\nRóznica między maks a min okrążenia: {dif_max_min_speed:.2f}s\nŚrednia prędkość w km/h: {avg_speed:.2f}km/h\n\nCzas aby pokonać 5km: \nMinuty: {minutes}\nSekundy: {seconds:.2f}")