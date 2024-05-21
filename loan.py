import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def montant_emprunt(mensualite, duree_annees, taux_annuel):
    """
    Calcule le montant maximal que l'on peut emprunter pour une mensualité donnée, une durée en années et un taux d'intérêt annuel.

    :param mensualite: Mensualité maximale (en euros)
    :param duree_annees: Durée du prêt (en années)
    :param taux_annuel: Taux d'intérêt annuel (en pourcentage)
    :return: Montant maximal empruntable (en euros)
    """
    # Convertir la durée en mois
    duree_mois = duree_annees * 12

    # Convertir le taux annuel en taux mensuel
    taux_mensuel = taux_annuel / 100 / 12

    # Formule de calcul du montant empruntable
    montant = mensualite * ((1 - (1 + taux_mensuel) ** -duree_mois) / taux_mensuel)

    return montant
    
def calculer_mensualite(montant_emprunte, duree_annees, taux_annuel):
    """
    Calcule la mensualité pour un montant emprunté donné, une durée en années et un taux d'intérêt annuel.

    :param montant_emprunte: Montant emprunté (en euros)
    :param duree_annees: Durée du prêt (en années)
    :param taux_annuel: Taux d'intérêt annuel (en pourcentage)
    :return: Mensualité (en euros)
    """
    # Convertir la durée en mois
    duree_mois = duree_annees * 12

    # Convertir le taux annuel en taux mensuel
    taux_mensuel = taux_annuel / 100 / 12

    # Formule de calcul de la mensualité
    mensualite = montant_emprunte * (taux_mensuel / (1 - (1 + taux_mensuel) ** -duree_mois))

    return mensualite
    
def tracer_courbe_mensualite(montant_emprunte, duree_annees):
    """
    Trace la courbe montrant l'évolution de la mensualité en fonction du taux d'intérêt pour un montant emprunté et une durée donnés.

    :param montant_emprunte: Montant emprunté (en euros)
    :param duree_annees: Durée du prêt (en années)
    """
    taux_interets = np.linspace(0.01, 10, 100)  # Taux d'intérêt de 0.1% à 10%
    mensualites = [calculer_mensualite(montant_emprunte, duree_annees, taux) for taux in taux_interets]

    plt.figure(figsize=(10, 6))
    plt.plot(taux_interets, mensualites, label=f'Mensualité pour {montant_emprunte}€ sur {duree_annees} ans')
    plt.title('Évolution de la mensualité en fonction du taux d\'intérêt')
    plt.xlabel('Taux d\'intérêt (%)')
    plt.ylabel('Mensualité (€)')
    plt.grid(True)
    plt.legend()
    plt.show()

def cout_total_pret(mensualite, duree_annees):
    """
    Calcule le coût total du prêt, y compris les intérêts payés sur toute la durée du prêt.

    :param mensualite: Mensualité (en euros)
    :param duree_annees: Durée du prêt (en années)
    :return: Coût total du prêt (en euros)
    """
    duree_mois = duree_annees * 12
    cout_total = mensualite * duree_mois
    return cout_total

def tableau_amortissement(montant_emprunte, duree_annees, taux_annuel):
    """
    Génère un tableau d'amortissement pour un prêt donné.

    :param montant_emprunte: Montant emprunté (en euros)
    :param duree_annees: Durée du prêt (en années)
    :param taux_annuel: Taux d'intérêt annuel (en pourcentage)
    :return: DataFrame contenant le tableau d'amortissement
    """
    duree_mois = duree_annees * 12
    taux_mensuel = taux_annuel / 100 / 12
    mensualite = calculer_mensualite(montant_emprunte, duree_annees, taux_annuel)
    
    amortissement = []
    principal_restant = montant_emprunte

    for mois in range(1, duree_mois + 1):
        interet = principal_restant * taux_mensuel
        principal = mensualite - interet
        principal_restant -= principal
        amortissement.append([mois, mensualite, principal, interet, principal_restant])

    df = pd.DataFrame(amortissement, columns=["Mois", "Mensualité", "Principal", "Intérêt", "Principal Restant"])
    return df
    
"""

# Exemple d'utilisation
mensualite_max = float(sys.argv[1])
duree_pret = int(sys.argv[2])
taux_interet = float(sys.argv[3])

montant = montant_emprunt(mensualite_max, duree_pret, taux_interet)
print(f"Pour une mensualité de {mensualite_max}€, une durée de {duree_pret} ans et un taux d'intérêt de {taux_interet}%, "
      f"vous pouvez emprunter au maximum : {montant:.2f}€")


montant_emprunte = 200000  # en euros
duree_pret = 20  # en années

tracer_courbe_mensualite(montant_emprunte, duree_pret)

mensualite = calculer_mensualite(200000, 20, 2.5)
cout_total = cout_total_pret(mensualite, 20)
print(f"Le coût total du prêt est de : {cout_total:.2f}€")
"""

# Exemple d'utilisation
amortissement_df = tableau_amortissement(200000, 20, 2.5)
print(amortissement_df.head())  # Affiche les premières lignes du tableau d'amortissement
