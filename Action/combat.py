from colorama import Fore, Style, init
from Instance.session import Session
from Action.attacker import Attacker
from Action.CombatMixin.tour_joueur import TourJoueurMixin
from Action.CombatMixin.tour_mobs import TourMobsMixin

init()

class combat(TourMobsMixin, TourJoueurMixin):
    def __init__(self, mobs):
        self.Mobs = Attacker(mobs)
        self.Joueur = self.Mobs
        print(
            Fore.MAGENTA + f"---Combats VS {self.Mobs.Mobs.Nom} ---\n" + Style.RESET_ALL+
            "\n"
            f"Vos vie : {Session.joueur.checkPV()} Coeur\n"
            f"Zombie vie : {self.Mobs.Mobs.Vie} Coeur\n"
            "\n"
        )

        self.tour_joueur()

        

        