from Instance.session import Session
from Models.item import Item
from colorama import Fore, Style, init
from Outils.temps import compte_a_rebours
import random

init()

class Miner:

    def minerBois():
        bois = 5
        temps = 45 / Session.joueur.checkOutil("Hache","Temps")

        compte_a_rebours(temps)

        print(
            Fore.YELLOW + f"Terminer! vous récolter {bois} de bois.\n"
            "\n" + Style.RESET_ALL
        )

        Session.joueur.modifier_inventaire("Bois", bois)
        Session.joueur.modifier_outil("Hache", durabiliter=1)
        Session.joueur.modifier_statistique("Bois", bois)

    def minerPierre():
        pierre = 3
        temps = 90 / Session.joueur.checkOutil("Pioche","Temps")

        compte_a_rebours(temps)

        print(
            Fore.YELLOW + f"Vous avez miner du bois, vous récolter {pierre} de bois.\n"
            "\n" + Style.RESET_ALL
        )

        Session.joueur.modifier_inventaire("Pierre", pierre)
        Session.joueur.modifier_outil("Pioche", durabiliter= 1)
        Session.joueur.modifier_statistique("Pierre", pierre)

    def minerDiamant():
        diamant = random.randint(1, 3)
        temps = 180 / Session.joueur.checkOutil("Pioche","Temps")

        compte_a_rebours(temps)

        print(
            Fore.YELLOW + f"Vous avez miner du bois, vous récolter {diamant} de bois.\n"
            "\n" + Style.RESET_ALL
        )

        Session.joueur.modifier_inventaire("Diamant", diamant)
        Session.joueur.modifier_outil("Pioche", durabiliter= 1)
        Session.joueur.modifier_statistique("Diamant", diamant)