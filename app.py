from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# load model pipeline
model = joblib.load("model_pipeline.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # IMPORTANT: نفس أسماء الأعمدة ديال التدريب
    input_df = pd.DataFrame([{
        "Année": data["Année"],
        "Mois": data["Mois"],
        "Semaine": data["Semaine"],
        "Heure_num": data["Heure_num"],
        "Machine_ID": data["Machine_ID"],
        "Jour_ID": data["Jour_ID"],
        "Shift_ID": data["Shift_ID"],
        "Categorie_Duree_ID": data["Categorie_Duree_ID"],
        "Duree_Arret_h": data["Duree_Arret_h"],
        "Nb_pannes_sem_prec": data["Nb_pannes_sem_prec"],
        "Moy_duree_arret_h": data["Moy_duree_arret_h"],
        "Temp_Armoire_moy": data["Temp_Armoire_moy"],
        "Temp_Moteur_moy": data["Temp_Moteur_moy"],
        "Ampeerage_moy": data["Ampeerage_moy"]
    }])

    prediction = model.predict(input_df)[0]

    return jsonify({
        "prediction": float(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)