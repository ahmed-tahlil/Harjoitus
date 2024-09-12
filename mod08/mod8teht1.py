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
# määritellään funktio

def fetch_airport_by_icao(code):
    sql = (f"SELECT name, municipality "
          f" FROM airport WHERE ident ='{code}'")
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    # palauttaa monikon, paitsi jos tyhjä tulosjoukko -> None
    return result_row

airport = fetch_airport_by_icao("ZYTH")

user_input = input("Anna ICAO-koodi: ")
airport = fetch_airport_by_icao(user_input)
#print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}.")

# jos airport-muuttujassa on jotain muuta kuin None/False/0

if airport: # vastaava: airport != None
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}.")
else:
    print("Lenttokenttää ei löydetty annetulla koodilla.")

# extra: tiedon lisäys

#def add_airport(icao,name):
   # sql = (f"INSERT INTO airport (id, ident, name, municipality)"
    #       f"VALUES (999, '{icao}', '{name}', '{municipality}');")
    #cursor = connection.cursor()
    #cursor.execute(sql)

#icao = input("Anna uusi ICAO: ")
#name = input("Anna uuden kentän nimi: ")
#municipality = input("Ja paikkakunta: ")

#add_airport(icao, name, municipality)