import json

def enregistrer_donnees(chemin, donnees):
    with open(chemin.value, 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)

def lire_fichier(chemin):
    with open(chemin.value, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
    return donnees