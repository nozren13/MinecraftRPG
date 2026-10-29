from Outils import json, chemin

class Item:

    def __init__(self):
        self.Equipement = json.lire_fichier(chemin.ItemChemin.EQUIPEMENT)
        self.Outils = json.lire_fichier(chemin.ItemChemin.OUTILS)
        self.Donjon = json.lire_fichier(chemin.ItemChemin.DONJON)
        self.Nourriture = json.lire_fichier(chemin.ItemChemin.NOURRITURE)

    def getItem(self, Item, Type):
        if Item in self.Donjon:
            return self.Donjon[Item][Type]
        
        elif Item in self.Equipement:
            return self.Equipement[Item][Type]

        elif Item in self.Outils:
            return self.Outils[Item][Type]

        elif Item in self.Nourriture:
            return self.Nourriture[Item][Type]
        
        else:
            return None