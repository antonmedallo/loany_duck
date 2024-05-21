from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autoriser les requêtes CORS

@app.route('/calculer-mensualite', methods=['POST'])
def calculer_mensualite():
    try:
        data = request.json
        print("Données reçues :", data)  # Log des données reçues
        montant_emprunte = float(data['montant_emprunte'])
        duree_annees = int(data['duree_annees'])
        taux_annuel = float(data['taux_annuel'])
        
        mensualite = calculer_mensualite_fonction(montant_emprunte, duree_annees, taux_annuel)
        print("Mensualité calculée :", mensualite)  # Log du résultat
        return jsonify({'mensualite': mensualite})
    except Exception as e:
        print("Erreur lors du calcul de la mensualité :", e)  # Log de l'erreur
        return jsonify({'error': str(e)}), 500

def calculer_mensualite_fonction(montant_emprunte, duree_annees, taux_annuel):
    duree_mois = duree_annees * 12
    taux_mensuel = taux_annuel / 100 / 12
    mensualite = montant_emprunte * (taux_mensuel / (1 - (1 + taux_mensuel) ** -duree_mois))
    return mensualite

if __name__ == '__main__':
    app.run(debug=True)
