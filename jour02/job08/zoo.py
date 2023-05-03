import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="zoo"
)

cursor = db.cursor()

def ajouter_animal():
    id = input("Entrez l'identifiant de l'animal : ")
    nom = input("Entrez le nom de l'animal : ")
    race = input("Entrez la race de l'animal : ")
    id_cage = input("Entrez l'identifiant de la cage de l'animal : ")
    date_naissance = input("Entrez la date de naissance de l'animal (format YYYY-MM-DD) : ")
    pays_origine = input("Entrez le pays d'origine de l'animal : ")
    
    query = "INSERT INTO animal (id, nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id, nom, race, id_cage, date_naissance, pays_origine)
    cursor.execute(query, values)
    db.commit()
    
def supprimer_animal():
    id = input("Entrez l'identifiant de l'animal à supprimer : ")
    
    query = "DELETE FROM animal WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    db.commit()
    
def modifier_animal():
    id = input("Entrez l'identifiant de l'animal à modifier : ")
    nom = input("Entrez le nouveau nom de l'animal : ")
    race = input("Entrez la nouvelle race de l'animal : ")
    id_cage = input("Entrez le nouvel identifiant de la cage de l'animal : ")
    date_naissance = input("Entrez la nouvelle date de naissance de l'animal (format YYYY-MM-DD) : ")
    pays_origine = input("Entrez le nouveau pays d'origine de l'animal : ")
    
    query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
    values = (nom, race, id_cage, date_naissance, pays_origine, id)
    cursor.execute(query, values)
    db.commit()
    
def afficher_animaux():
    query = "SELECT * FROM animal"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
        
def afficher_animaux_cages():
    query = "SELECT animal.nom, cage.id FROM animal LEFT JOIN cage ON animal.id_cage = cage.id"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
        
def ajouter_cage():
    id = input("Entrez l'identifiant de la cage : ")
    superficie = input("Entrez la superficie de la cage : ")
    capacite_max = input("Entrez la capacité maximale de la cage : ")
    
    query = "INSERT INTO cage (id, superficie, capacite_max) VALUES (%s, %s, %s)"
    values = (id, superficie, capacite_max)
    cursor.execute(query, values)
    db.commit()

def supprimer_cage():
    id = input("Entrez l'identifiant de la cage à supprimer : ")
    
    query = "DELETE FROM cage WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    db.commit()

def modifier_cage():
    id = input("Entrez l'identifiant de la cage à modifier : ")
    superficie = input("Entrez la nouvelle superficie de la cage : ")
    capacite_max = input("Entrez la nouvelle capacité maximale de la cage : ")
    
    query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
    values = (superficie, capacite_max, id)
    cursor.execute(query, values)
    db.commit()

def calculer_superficie_totale():
    query = "SELECT SUM(superficie) FROM cage"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    print("La superficie totale de toutes les cages est :", result, "m²")

while True:
    choix = input("Que souhaitez-vous faire ?\n1. Ajouter un animal\n2. Supprimer un animal\n3. Modifier un animal\n4. Afficher la liste des animaux\n5. Afficher la liste des animaux dans les cages\n6. Ajouter une cage\n7. Supprimer une cage\n8. Modifier une cage\n9. Calculer la superficie totale des cages\n10. Quitter\n")
    
    if choix == "1":
        ajouter_animal()
    elif choix == "2":
        supprimer_animal()
    elif choix == "3":
        modifier_animal()
    elif choix == "4":
        afficher_animaux()
    elif choix == "5":
        afficher_animaux_cages()
    elif choix == "6":
        ajouter_cage()
    elif choix == "7":
        supprimer_cage()
    elif choix == "8":
        modifier_cage()
    elif choix == "9":
        calculer_superficie_totale()
    elif choix == "10":
        break
    else:
        print("Choix invalide")


