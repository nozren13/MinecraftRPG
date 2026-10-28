from Models.joueur import Joueur

class Session:
    joueur = None

    @classmethod
    def setJoueur(cls, Email):
        cls.joueur = Joueur(Email)