from colorama import Fore, Style, init

init()

class AchatEquipementMixin:
    def achatEquipement(self):
        while(True):
            print(
                Fore.GREEN + " -- Achat/Equipement -- \n" + Style.RESET_ALL +
                "\n"
                "Article : Casque / Plastron / Jambiére / Botte \n"
                "\n"
                )

            choix = input("Quel article voulez vous acheter : ")
            print("\n")

            
