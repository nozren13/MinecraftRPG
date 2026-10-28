class JoueurCheckMixin:

    def checkPotion(self):
        return self.Outils["Potion"] 
    
    def checkPV(self):
        return self.Compte["Vie"]
    
    def checkCompte(self, Clé):
        return self.Compte[Clé]

    def checkInventaire(self, Objet):
        return self.Inventaire[Objet]

    def checkEquipement(self, Equipement, Catégorie):
        return self.Equipement[Equipement][Catégorie]

    def checkOutil(self, Outil, Catégorie):
        return self.Outils[Outil][Catégorie]

    def checkClé(self, Difficulté):
        return self.Inventaire["Clé_Donjon"][Difficulté]

    def checkStats(self, Stats):
        return self.Statistique[Stats]