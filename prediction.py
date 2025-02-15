import pandas as pd
import sqlite3

def charger_donnees():
    conn = sqlite3.connect("ventes.db")
    df = pd.read_sql_query("SELECT * FROM ventes", conn)
    conn.close()
    return df

# Tester si ça fonctionne
df = charger_donnees()
print(df.head())