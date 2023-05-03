import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "plomkiplomki",
    database = "LaPlatforme"
)

mycursor = db.cursor()

mycursor.execute("SELECT nom, capacite FROM salles")

resultats = mycursor.fetchall()

for resultat in resultats:
    print(resultat[0], resultat[1])


db.close()