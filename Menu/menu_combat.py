from colorama import Fore, Style, init
from Action.combat import combat
from Instance.session import Session

init()

def menu_combat():
    while(True):
        if Session.joueur.checkPV() <= 0:
            print(Fore.RED + "Vous êtes mort, attendez la régénération.\n" + Style.RESET_ALL)
            break

        print(
            Fore.GREEN + "---Comabts--- \n" + Style.RESET_ALL +
            "\n"
            "1 - Zombie\n"
            "2 - Squelette\n"
            "3 - Creeper\n"
            "4 - Retour"
            "\n"
        )

        try:
            option = int(input("Quelle action voulez-vous faire(1 à 4) : "))
            print("\n")
        except ValueError:
            print(Fore.RED + "Erreur. Merci de donnez un chiffre \n" + Style.RESET_ALL)
            continue
        
        if option == 1:
            combat("Zombie")
        elif option == 2 :
            combat("Squelette")
        elif option == 3 :
            combat("Creeper")
        elif option == 4 :
            print(Fore.CYAN+"Retour\n"+Style.RESET_ALL )
            break
        else :
            print( Fore.RED+ "Donnez un chiffre entre 1 et 4."+Style.RESET_ALL)
        