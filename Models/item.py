from Outils import json, chemin

class Item:

    def __init__(self):
        self.Equipement = json.lire_fichier(chemin.ItemChemin.EQUIPEMENT)
        self.Outils = json.lire_fichier(chemin.ItemChemin.OUTILS)
        self.Clé_Donjon = json.lire_fichier(chemin.ItemChemin.CLE_DONJON)

    def getPotion(self):
        return self.Outils["Potion"]

    def getEquipement(self, Equipement, Type):
        return self.Equipement[Equipement][Type]

    def getOutils(self, Outils, Type):
        return self.Outils[Outils][Type]

    def getCléDonjon(self, difficulté):
        return self.Clé_Donjon[difficulté]