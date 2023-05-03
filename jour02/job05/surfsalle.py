import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "plomkiplomki",
    database = "LaPlatforme"
)

mycursor = db.cursor()

query = "SELECT SUM(superficie) AS superficie_totale FROM etage;"
mycursor.execute(query)

resultat = mycursor.fetchone()[0]

print("La superficie de La Plateforme est de", resultat, "m2")

db.close()