from colorama import Fore, Style, init
from Menu.menu_compte import creation_compte, connexion

init()

while(True):
    print(
        Fore.GREEN + "---Bienvenue dans l'acceuil de Minecraft RPG---\n" + Style.RESET_ALL +
        "\n" +
        "1 | Création de compte\n"
        "2 | Connexion \n"
        "3 | Fermer le programme\n"
        "\n"
        )

    try :
        option = int(input("Qu'est ce que voulez vous faire(1 à 3): "))
        print("\n")
    except ValueError :
        print(Fore.RED + "Erreur. Merci de donnez un chiffre \n" + Style.RESET_ALL)
        continue

    if(option == 1 ):
        creation_compte()
    elif(option == 2):
        connexion()
    elif(option == 3):
        print(Fore.CYAN + "Le programme est bien términer, merci d'y avoir jouer! \n" + Style.RESET_ALL)
        break


    

