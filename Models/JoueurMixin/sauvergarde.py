from Outils import json, chemin

class SauvergardeMixin:
    def _sauvegarder_Compte(self):
        compte = json.lire_fichier(chemin.JoueurChemin.COMPTE)
        compte[self.Email] = self.Compte
        json.enregistrer_donnees(chemin.JoueurChemin.COMPTE, compte)

    def _sauvegarder_inventaire(self):
        inventaire = json.lire_fichier(chemin.JoueurChemin.INVENTAIRE)
        inventaire[self.Email] = self.Inventaire
        json.enregistrer_donnees(chemin.JoueurChemin.INVENTAIRE, inventaire)

    def _sauvegarder_statistique(self):
        statistique = json.lire_fichier(chemin.JoueurChemin.INVENTAIRE)
        statistique[self.Email] = self.Statistique
        json.enregistrer_donnees(chemin.JoueurChemin.STATISTIQUE, statistique)

    def _sauvegarder_outil(self):
        outil = json.lire_fichier(chemin.JoueurChemin.OUTILS)
        outil[self.Email] = self.Outils
        json.enregistrer_donnees(chemin.JoueurChemin.OUTILS, outil)

    def _sauvegarder_equipement(self):
        equipement = json.lire_fichier(chemin.JoueurChemin.EQUIPEMENT)
        equipement[self.Email] = self.Equipement
        json.enregistrer_donnees(chemin.JoueurChemin.EQUIPEMENT, equipement)   

    def _sauvegarder_quete(self):
        quete = json.lire_fichier(chemin.JoueurChemin.QUETES)
        quete[self.Email] = self.Quetes
        json.enregistrer_donnees(chemin.JoueurChemin.QUETES, quete)

    def _sauvegarder_succes(self):
        succes =json.lire_fichier(chemin.JoueurChemin.SUCCES)
        succes[self.Email] = self.Quetes
        json.enregistrer_donnees(chemin.JoueurChemin.SUCCES, succes)