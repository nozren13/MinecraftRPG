from enum import Enum

class EntiteChemin(Enum):
    ZOMBIE = 'Data/Entite/zombie.json'
    SQUELETTE = 'Data/Entite/squelette.json'
    CREEPER = 'Data/Entite/crepper.json'

class ItemChemin(Enum):
    EQUIPEMENT = 'Data/Item/equipement.json'
    CLE_DONJON = 'Data/Item/cle_donjon.json'
    OUTILS = 'Data/Item/outils.json'

class JoueurChemin(Enum):
    MODEL = 'Data/Joueur/model.json'
    COMPTE = 'Data/Joueur/compte.json'
    EQUIPEMENT = 'Data/Joueur/equipement.json'
    OUTILS = 'Data/Joueur/outils.json'
    INVENTAIRE = 'Data/Joueur/inventaire.json'
    QUETES = 'Data/Joueur/quetes.json'
    SUCCES = 'Data/Joueur/succes.json'
    STATISTIQUE ='Data/Joueur/statistique.json'

class ServiceChemin(Enum):
    SUCCES = 'Data/Services/succes.json'
    QUETES = 'Data/Services/quetes.json'
