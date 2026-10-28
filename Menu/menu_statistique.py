from colorama import Fore, Style, init
from Instance.session import Session

init()

def menu_statistique():
    print(
        Fore.GREEN + " -- Statistique -- \n" + Style.RESET_ALL
        +Fore.CYAN + "- Objets - \n"+ Style.RESET_ALL +
        "\n"
        f"Bois : {Session.joueur.checkStats('Bois')} \n"
        f"Pierre : {Session.joueur.checkStats('Pierre')} \n"
        f"Diamant : {Session.joueur.checkStats('Diamant')} \n"
        "\n"
        +Fore.CYAN + "- Mobs - \n"+ Style.RESET_ALL +
        "\n"
        f"Zombie: {Session.joueur.checkStats('Zombie')} \n"
        f"Squelette: {Session.joueur.checkStats('Squelette')} \n"
        f"Creeper: {Session.joueur.checkStats('Creeper')} \n"
        "\n"
        )
    while (True):
        choix = input("Voulez-vous retournez en arriére?(oui/non) : ").strip().lower()
        print("\n")

        if choix == "oui":
            print(Fore.CYAN + "Retour \n" + Style.RESET_ALL)
            break
        else:
            continue