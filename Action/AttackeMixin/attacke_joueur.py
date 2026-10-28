from Outils.temps import arriére_plan_compte_a_rebours
from colorama import Fore, Style, init
from Instance.session import Session
from Models.item import Item

init()

class AttackeJoueurMixin:

    def calculer_dégats_joueur(self):
            return Session.joueur.checkOutil("Epee", "Attacke")

    def joueur_attacker_mobs(self):
        dégats = self.calculer_dégats_joueur()
        vieMobs = self.Mobs.Vie - dégats
        self.Mobs.dégatSubis(dégats)

        if vieMobs <= 0:
            argent, xp = self.Mobs.getRécompense()
            print(
                Fore.GREEN +" --  WINNER -- \n"+ Style.RESET_ALL +
                "\n"
                "Vous avez gagnéz, bravo! Voici vos récompense :\n"
                f"- Argent : {argent} \n"
                f"- Xp : {xp} \n"
                "\n"
                )
            Session.joueur.modifier_Compte("Vie", 100)
            Session.joueur.ajoutRécompense(argent, xp)
            Session.joueur.modifier_statistique(self.Mobs.Nom, 1)
            return True
        else:
            print(f"Vous lui avez infligué {dégats}, il lui reste {vieMobs}.\n" +"\n")
            return False
