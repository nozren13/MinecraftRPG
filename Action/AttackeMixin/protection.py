from Instance.session import Session
from Models.item import Item

class ProtectionMixin:

    def calculer_protection(self):
            Equipements = ["Plastron", "Jambiére" , "Casque", "Botte"]
            Protection = 0
        
            for Equipement in Equipements:
                Protection += Session.joueur.checkEquipement(Equipement, "Protection")
        
            return 1 if Protection<=0 else Protection * 4/100