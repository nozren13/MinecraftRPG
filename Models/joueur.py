from Outils import chemin, json
from Models.JoueurMixin.modification import ModificationMixin
from Models.JoueurMixin.profil import JoueurProfilMixin
from Models.JoueurMixin.compte import JoueurCompteMixin
from Models.JoueurMixin.check import JoueurCheckMixin
from Models.JoueurMixin.ajout_récompense import AjoutRécompenseMixin

class Joueur(ModificationMixin, JoueurProfilMixin, JoueurCompteMixin, JoueurCheckMixin, AjoutRécompenseMixin):

    def __init__(self, Email):
        self.Email = Email
        self.Compte = json.lire_fichier(chemin.JoueurChemin.COMPTE)[Email]
        self.Inventaire = json.lire_fichier(chemin.JoueurChemin.INVENTAIRE)[Email]
        self.Statistique = json.lire_fichier(chemin.JoueurChemin.STATISTIQUE)[Email]
        self.Outils = json.lire_fichier(chemin.JoueurChemin.OUTILS)[Email]
        self.Equipement = json.lire_fichier(chemin.JoueurChemin.EQUIPEMENT)[Email]
        self.Quetes = json.lire_fichier(chemin.JoueurChemin.QUETES)[Email]
        self.Succes = json.lire_fichier(chemin.JoueurChemin.SUCCES)[Email]
        self._ajouter_xp(0)
