from flask import Flask, request, jsonify
from calculs_pret import calculer_mensualite, tableau_amortissement

app = Flask(__name__)

@app.route('/calculer-mensualite', methods=['POST'])
def calculer_mensualite_route():
    data = request.json
    montant_emprunte = data['montant_emprunte']
    duree_annees = data['duree_annees']
    taux_annuel = data['taux_annuel']
    mensualite = calculer_mensualite(montant_emprunte, duree_annees, taux_annuel)
    return jsonify({'mensualite': mensualite})

@app.route('/tableau-amortissement', methods=['POST'])
def tableau_amortissement_route():
    data = request.json
    montant_emprunte = data['montant_emprunte']
    duree_annees = data['duree_annees']
    taux_annuel = data['taux_annuel']
    df = tableau_amortissement(montant_emprunte, duree_annees, taux_annuel)
    amortissement = df.to_dict(orient='records')
    return jsonify({'amortissement': amortissement})

if __name__ == '__main__':
    app.run(debug=True)
