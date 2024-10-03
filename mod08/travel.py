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




def travel(airports, money, co2, day):
    available_airports = check_airport_co2_level(airports, co2)
    closest_airports = get_closest_airports(available_airports)

