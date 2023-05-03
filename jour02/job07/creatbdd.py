import mysql.connector


class EmployesManager:
    def __init__(self):
        # Configuration de la connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="votre_utilisateur",
            password="votre_mot_de_passe",
            database="votre_base_de_donnees"
        )
        self.cursor = self.conn.cursor()

    def create(self, nom, prenom, salaire, id_service):
        # Requête SQL pour ajouter un nouvel employé
        sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        # Paramètres de la requête
        values = (nom, prenom, salaire, id_service)
        # Exécution de la requête
        self.cursor.execute(sql, values)
        # Validation de la transaction
        self.conn.commit()
        # Affichage d'un message de confirmation
        print(f"L'employé {nom} {prenom} a été ajouté avec succès !")

    def read(self, id=None):
        if id:
            # Requête SQL pour récupérer un employé en particulier
            sql = "SELECT * FROM employes WHERE id = %s"
            # Paramètres de la requête
            values = (id,)
            # Exécution de la requête
            self.cursor.execute(sql, values)
            # Récupération du résultat
            result = self.cursor.fetchone()
            # Affichage du résultat
            print(result)
        else:
            # Requête SQL pour récupérer tous les employés
            sql = "SELECT * FROM employes"
            # Exécution de la requête
            self.cursor.execute(sql)
            # Récupération de tous les résultats
            results = self.cursor.fetchall()
            # Affichage des résultats
            for result in results:
                print(result)

    def update(self, id, nom=None, prenom=None, salaire=None, id_service=None):
        # Requête SQL pour modifier un employé
        sql = "UPDATE employes SET"
        values = []
        if nom:
            sql += " nom = %s,"
            values.append(nom)
        if prenom:
            sql += " prenom = %s,"
            values.append(prenom)
        if salaire:
            sql += " salaire = %s,"
            values.append(salaire)
        if id_service:
            sql += " id_service = %s,"
            values.append(id_service)
        # Suppression de la dernière virgule
        sql = sql[:-1]
        # Ajout du critère de sélection
        sql += " WHERE id = %s"
        values.append(id)
        # Exécution de la requête
        self.cursor.execute(sql, tuple(values))
        # Validation de la transaction
        self.conn.commit()
        # Affichage d'un message de confirmation
        print(f"L'employé avec l'ID {id} a été modifié avec succès !")

    def delete(self, id):
        # Requête SQL pour supprimer un employé
        sql = "DELETE FROM employes WHERE id = %s"
        # Paramètres de la requête
        values = (id,)
        # Exécution de la requête
        self.cursor.execute(sql, values)
        # Validation de la transaction
        self.conn.commit()
