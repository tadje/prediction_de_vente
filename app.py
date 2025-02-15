from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Page pour ajouter une vente
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        date = request.form["date"]
        produit = request.form["produit"]
        prix = float(request.form["prix"])
        quantite = int(request.form["quantite"])

        # Ajouter la vente en base de données
        conn = sqlite3.connect("ventes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ventes (date, produit, prix, quantite) VALUES (?, ?, ?, ?)", 
                       (date, produit, prix, quantite))
        conn.commit()
        conn.close()
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
