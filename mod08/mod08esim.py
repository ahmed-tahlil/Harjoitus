import mysql.connector

import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1', #localhost
         port= 3306,
         database='flight_game',
         user='ahmed',
         password='salasana',
         autocommit=True,
        charset = 'utf8mb4',
         collation='utf8mb4_general_ci',
         )
#print(connection)
# luodaan osoitin ja sijoitetaan muuttujaan
cursor = connection.cursor()
# ajetaan SQL-kielinen kysely osoittimen avulla

cursor.execute("SELECT continent,name, iso_country FROM country")

result = cursor.fetchone()
print(result)

# fetchmany() palauttaa halutun määrän rivejä (monikko) kerrallaan listana
#result = cursor.fetchmany(3)
#print(result)

#fetchall () palauttaa kaikki loput rivit listana

rows = cursor.fetchall()
#print(rows)
print(f"Tulosrivejä yhteensä: {cursor.rowcount}")
# tuloslista käsitellään toistorakenteella
#for row in rows:
#print(row)  # Tulosta rivi nähdäksesi, mitä se sisältää
            #print(f"{row[1]}, Maakoodi: {row [2]}, maanosa: {row[0]}")
