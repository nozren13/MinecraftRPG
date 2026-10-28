from Outils import chemin, json
from Models.JoueurMixin.sauvergarde import SauvergardeMixin

class ModificationMixin(SauvergardeMixin):

    def modifier_Compte(self, cle, valeur):
        self.Compte[cle] = valeur
        self._sauvegarder_Compte()

    def modifier_inventaire(self, item, quantite):
        self.Inventaire[item] = self.Inventaire.get(item,0) + quantite
        self._sauvegarder_inventaire()

    def modifier_statistique(self, stat, quantite):
        self.Statistique[stat] += quantite
        self._sauvegarder_statistique

    def modifier_outil(self, outil, type = None, durabiliter = 0):
        if(outil == "Potion"):
            self.Outils[outil] = self.Outils.get(outil,0) + type 

        else :
            if durabiliter == 0 :
                self.Outils[outil] = type

            else :
                self.Outils[outil]["Durabiliter"] -= durabiliter

                if self.Outils[outil]["Durabiliter"] <= 0 :
                    self.Outils[outil] = json.lire_fichier(chemin.ItemChemin.OUTILS)[outil][""]

        self._sauvegarder_outil()

    def modfier_equipement(self, equipement, type):
        self.Equipement[equipement] = type
        self._sauvegarder_equipement

    def modifier_quete(self, quete, boolean):
        self.Quetes[quete] = boolean
        self._sauvegarder_quete()

    def modifier_succes(self, succes, boolean):
        self.Succes[succes] = boolean
        self._sauvegarder_succes()