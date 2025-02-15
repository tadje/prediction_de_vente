import sqlite3

# Connexion à la base de données (créera un fichier si inexistant)
conn = sqlite3.connect("ventes.db")
cursor = conn.cursor()

# Création de la table des ventes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        produit TEXT,
        prix REAL,
        quantite INTEGER
    )
""")

conn.commit()
conn.close()
print("Base de données créée avec succès !")