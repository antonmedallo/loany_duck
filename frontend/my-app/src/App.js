import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [montantEmprunte, setMontantEmprunte] = useState('');
    const [dureeAnnees, setDureeAnnees] = useState('');
    const [tauxAnnuel, setTauxAnnuel] = useState('');
    const [mensualite, setMensualite] = useState(null);
    const [error, setError] = useState(null);

    const calculerMensualite = async () => {
        try {
            const response = await axios.post('http://localhost:5000/calculer-mensualite', {
                montant_emprunte: montantEmprunte,
                duree_annees: dureeAnnees,
                taux_annuel: tauxAnnuel
            });
            setMensualite(response.data.mensualite);
            setError(null);
        } catch (error) {
            setError(error.response ? error.response.data : error.message);
            console.error("Erreur lors du calcul de la mensualité :", error);
        }
    };

    return (
        <div className="App">
            <h1>Calculateur de Prêt Immobilier</h1>
            <div>
                <label>Montant Emprunté :</label>
                <input type="number" value={montantEmprunte} onChange={(e) => setMontantEmprunte(e.target.value)} />
            </div>
            <div>
                <label>Durée (années) :</label>
                <input type="number" value={dureeAnnees} onChange={(e) => setDureeAnnees(e.target.value)} />
            </div>
            <div>
                <label>Taux Annuel (%) :</label>
                <input type="number" value={tauxAnnuel} onChange={(e) => setTauxAnnuel(e.target.value)} />
            </div>
            <button onClick={calculerMensualite}>Calculer Mensualité</button>
            {mensualite && <div>Mensualité : {mensualite.toFixed(2)} €</div>}
            {error && <div style={{color: 'red'}}>Erreur : {error}</div>}
        </div>
    );
}

export default App;
