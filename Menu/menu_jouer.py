from colorama import Fore, Style, init
from Menu.menu_miner import menu_miner 
from Instance.session import Session
from Menu.menu_combat import menu_combat
from Menu.menu_profil import menu_profil
from Menu.menu_inventaire import menu_inventaire
from Menu.menu_statistique import menu_statistique
from Menu.menu_boutique import boutique

init()

def menu_jouer():
    while(True):
        print(
            Fore.GREEN + "---MinecraftRPG---\n" + Style.RESET_ALL +
            "\n"
            "1 - Profil \n"
            "2 - Inventaire \n"
            "3 - Minage \n"
            "4 - Combat \n"
            "5 - Stats \n"
            "6 - Boutique \n"
            "7 - Quêtes \n"
            "8 - Succès \n"
            "\n"
            )

        try :
            option = int(input("Quelle action voulez-vous faire (1 à 8) : "))
            print("\n")
        except ValueError:
            print(Fore.RED + "Erreur. Merci de donnez un chiffre \n" + Style.RESET_ALL)
            continue

        if option == 1:
            menu_profil()
        elif option == 2 :
            menu_inventaire()
        elif option == 3:
            menu_miner()
        elif option == 4:
            menu_combat()
        elif option == 5:
            menu_statistique()
        elif option == 6:
            boutique()
        elif option == 7:
            Session.joueur.getQuetes()
        elif option == 8:
            Session.joueur.getSucces()
        else :
            print( Fore.RED+ "Donnez un chiffre entre 1 et 8."+Style.RESET_ALL)
