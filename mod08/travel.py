from geopy.distance import distance

#### lentokenttien co2
def check_airport_co2_level(airports, co2):
    co2_deg = round(co2/100)  ### co2 laskuri

    available_airports = []  #### käytettävissä olevat kentät

    for airport in airports:
        if airport["latitude_deg"] > co2_deg:
            available_airports.append(airport)

    return available_airports



def get_closest_airports(p_id, airports):

    current_airport = player_location_full(p_id) # pelaajan nykyinen sijainti
    current_airport_coord = (current_airport["latitude_deg"], current_airport["longitude_deg"])

    airports_with_distances = []

    for airport in airports:
        airport_coord = (airport["latitude_deg"], airport["longitude_deg"])
        dist = distance(current_airport_coord, airport_coord).km #laskee etäisyyden

        airports_with_distances.append((airport, dist))

    # lähimmät lentokentät
    closest_airports = []

    while len(closest_airports) < 5 and airports_with_distances:
        min_dist = airports_with_distances[0][1]
        min_airport = airports_with_distances[0][0]
        for airport, dist in airports_with_distances:
            if dist < min_dist:
                min_dist = dist
                min_airport = airport

        # lisätään lähin lentokenttä listaan
        closest_airports.append(min_airport["Name"])
        airports_with_distances.remove(min_airport,min_dist)

    return closest_airports

def closest_airport(closest_airports):
    min_airport = closest_airports[0][0]
    min_dist = closest_airports[0][1]

    for airport, dist in closest_airports:
        if dist < min_dist:
            min_airport = airport
            min_dist = dist

    return min_airport




def travel(airports, money, co2, day):
    available_airports = check_airport_co2_level(airports, co2)
    if not available_airports:
        print("Cannot travel, do environment task")
        return environmental_task(money,co2,day)
    closest_airports = get_closest_airports(available_airports)

    travel_methods = {
        "1": {"method": "airplane", "money": 1000, "co2": 1000, "days": 1},
        "2": {"method": "train", "money": 500, "co2": 250, "days": 3},
        "3": {"method": "bicycle", "money": 100, "co2": 0, "days": 5}
    }

    print("Choose how you want to travel: ")
    print("1. Airplane (Cost: 1000€, CO2: 1000, Days: 1)")
    print("2. Train (Cost: 500€, CO2: 250, Days: 3)")
    print("3. Bicycle (Cost: 100€, CO2: 0, Days: 5)")

    method = input("How do you want to travel?")

    if method in travel_methods:
        travel_method = travel_methods[method]
        money = money - travel_method["money"]
        co2 = co2 - travel_method["co2"]
        day = day - travel_method["days"]

    else:
        print("Invalid input. Try again.")
        return travel(airports, money, co2, day)

    return money,co2,day




