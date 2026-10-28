from colorama import Fore, Style, init
from Models.item import Item

init()

class AcheterMixin:
    def acheterEquipementOutil(self):
        while(True):
            print(
                Fore.GREEN + " -- Acheter -- \n" + Style.RESET_ALL +
                "\n"
                "1 - Equipement \n"
                "2 - Outils \n"
                "3 - Clé Donjon \n"
                "4 - Retour \n"
                "\n"
            )
            try:
                option = int(input("Quelle action voulez-vous faire(1 à 4) : "))
                print("\n")
            except ValueError:
                print(Fore.RED + "Erreur. Merci de donnez un chiffre \n" + Style.RESET_ALL)
                continue

            if option == 1:
                continue
            elif option == 4:
                print(Fore.CYAN + " Retour \n" + Style.RESET_ALL)
                break
            else:
                print( Fore.RED+ "Donnez un chiffre entre 1 et 3.\n"+"\n"+Style.RESET_ALL)


    def acheterTyper(self, objet):
        while(True):
            print(
                Fore.GREEN + f" -- Acheter {objet} -- \n" + Style.RESET_ALL +
                "\n"
                ""
            )