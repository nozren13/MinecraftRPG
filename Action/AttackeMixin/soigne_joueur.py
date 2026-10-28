from Instance.session import Session
from Models.item import Item
from colorama import Fore, Style, init

init()

class SoigneJoueurMixin:
    def soignerJoueur(self):
        avoirPotion =  0 > Session.joueur.checkPotion()

        if avoirPotion :
            vie = Session.joueur.checkPV() + Item.getPotion
            Session.joueur.modifier_Compte("Vie", vie)
            Session.joueur.modifier_outil("Potion", -1)
            print(Fore.CYAN +  f"Vous avez avez utiliser une potion, vous étes a {vie} Coeurs\n" +Style.RESET_ALL + "\n")
            return False
        else : 
            print("Vous n'avez pas de potion.\n"+"\n")
            return True