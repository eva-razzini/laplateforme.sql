import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "plomkiplomki",
    database = "LaPlatforme"
)

mycursor = db.cursor()

mycursor.execute('SELECT SUM(capacite) AS total_capacite FROM salles')
resultat = mycursor.fetchone()[0]

print("La somme des capacités des salles est de", resultat)

db.close()