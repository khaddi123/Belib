import mysql.connector
import json

# Connexion à la base de données MySQL via MySQL Workbench
conn = mysql.connector.connect(
    host="localhost",       # Adresse de votre serveur MySQL
    user="root",
    password="H68bhxcx@",
    database="belib"
)
cursor = conn.cursor()

# Lire le fichier location.json
with open("C:/Users/Utilisateur/Desktop/Velib/location.json", "r") as json_file:
    data = json.load(json_file)

# Insérer les données dans la table belib_data
for station in data:
    if "nom" in station:
        nom_station = station["nom"]
    else:
        nom_station = "Nom inconnu"  # Défaut en cas de manque de clé
    latitude = station["latitude"]
    longitude = station["longitude"]
    cursor.execute(
        "INSERT INTO belib_data (nom_station, latitude, longitude) VALUES (%s, %s, %s)",
        (nom_station, latitude, longitude)
    )

# Commit des modifications
conn.commit()

print(f"{cursor.rowcount} lignes insérées avec succès")

# Fermeture de la connexion
cursor.close()
conn.close()


