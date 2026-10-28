from Outils.temps import arriére_plan_compte_a_rebours
from colorama import Fore, Style, init
from Instance.session import Session
from Models.item import Item

class AttackeMobsMixin():

    def caculer_dégats_mobs(self):
        protectiont = self.calculer_protection()
        dégatMobs = self.Mobs.dégatInfliguer() * protectiont
        return dégatMobs

    def mobs_attacker_joueur(self):
        dégats = self.caculer_dégats_mobs()
        Vie = Session.joueur.checkPV() - dégats
        Session.joueur.modifier_Compte("Vie", Vie)

        if Vie <= 0:
            arriére_plan_compte_a_rebours()
            print(
                Fore.RED + " -- GAME OVER -- \n" + Style.RESET_ALL +
                "Vous avez perdu, votre vie vas se regenere a fond dans 1h! \n" +"\n"
                )
            return False
        else:
            print(f"Le {self.Mobs.Nom} vous a infliguer {dégats} Dégats, il vous reste {Vie} Coeurs.\n"+"\n")
            return True