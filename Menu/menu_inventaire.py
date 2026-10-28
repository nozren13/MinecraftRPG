from colorama import Fore, Style, init
from Menu.menu_equipement import menu_equipement
from Menu.menu_outils import menu_outils
from Menu.menu_objets_cle import menu_objets_cle

init()

def menu_inventaire():
    while (True):
        print(
            Fore.GREEN + " -- Inventaire -- \n" + Style.RESET_ALL +  
            "\n"
            "1 - Equipement \n"
            "2 - Outils \n"
            "3 - Objets \n"
            "4 - Retour \n"
            "\n"
        )

        try : 
            option = int(input("Vous voulez regarder quoi (1 à 4): \n"))
            print("\n")
        except ValueError:
            print(Fore.RED + "Erreur. Merci de donnez un chiffre \n" + Style.RESET_ALL)
            continue

        if option == 1:
            menu_equipement()
        elif option == 2:
            menu_outils()
        elif option == 3:
            menu_objets_cle()
        elif option == 4:
            break
        else : 
            print( Fore.RED+ "Donnez un chiffre entre 1 et 4."+Style.RESET_ALL)