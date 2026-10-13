from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Route de calcul : reçoit les données envoyées (méthode POST)
@app.route("/calculer", methods=["POST"])
def calculer():
    # 1. Récupération des données saisies dans le formulaire
    moyen_transport = request.form.get("transport")
    distance = float(request.form.get("distance", 0))

    # 2. Facteurs d'émission (en kg de CO2 par km)
    facteurs = {
        "voiture": 0.21,
        "train": 0.003,
        "avion": 0.26
    }

    # 3. Calcul
    co2_par_km = facteurs.get(moyen_transport, 0)
    total_co2 = round(distance * co2_par_km, 2)

    # 4. Envoi des résultats à la page resultat.html
    return render_template(
        "resultat.html", 
        distance=distance, 
        transport=moyen_transport, 
        total=total_co2
    )
if __name__ == "__main__":
    app.run(debug=True)