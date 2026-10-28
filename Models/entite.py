from Outils import json, chemin
from colorama import Fore, Style, init

init()

class Entite:

    def __init__(self, entite):
        cheminEntite = getattr(chemin.EntiteChemin, entite.upper())
        donnees = json.lire_fichier(cheminEntite)

        self.Nom = donnees["Entité"]
        self.Vie = donnees["Vie"]
        self.Degats = donnees["Dégat"]
        self.Attacke = donnees["NombreAttacke"]
        self.Recompense = donnees["Récompense"]

    def dégatSubis(self, quantite):
        self.Vie -= quantite
        print(Fore.MAGENTA + f"L'entite {self.Nom} a pris {quantite} dégats, il lui reste plus que {self.Vie}. \n" + Style.RESET_ALL + "\n")

    def dégatInfliguer(self):
        return self.Degats

    def nombreAttcke(self):
        return self.Attacke

    def getRécompense(self):
        return self.Recompense["Argent"], self.Recompense["Xp"]


