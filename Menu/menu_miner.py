from colorama import Fore, Style, init
from Action.miner import Miner

init()
def menu_miner():
    while(True):
        print(
            Fore.GREEN + "---Minage---\n" + Style.RESET_ALL +
            "\n"
            "1 - Bois \n"
            "2 - Pierre \n"
            "3 - Diamants \n"
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
            Miner.minerBois()
        elif option == 2 :
            Miner.minerPierre()
        elif option == 3 :
            Miner.minerDiamant()
        elif option == 4 :
            print(Fore.CYAN+"Retour\n"+Style.RESET_ALL )
            break
        else :
            print( Fore.RED+ "Donnez un chiffre entre 1 et 4."+Style.RESET_ALL)