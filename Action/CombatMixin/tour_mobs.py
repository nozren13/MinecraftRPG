from Models.entite import *
import random

class TourMobsMixin:

    def tour_mobs(self):
        nombreAttacke = self.Mobs.Mobs.nombreAttcke()

        if nombreAttacke == 0 or random.randint(0, 10) == 4:
            return self.Mobs.mobs_attacker_joueur()

        print(f"Le {self.Mobs.Mobs.Nom} n'a pas attaqué, c'est à votre tour.\n")
        return True