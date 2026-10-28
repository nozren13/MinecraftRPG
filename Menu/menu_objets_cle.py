from colorama import Fore, Style, init
from Instance.session import Session

init()

def menu_objets_cle():
    print(
        Fore.GREEN + " -- Objets -- \n" + Style.RESET_ALL +
        "\n"
        f"Bois : {Session.joueur.checkInventaire('Bois')} \n"
        f"Pierre : {Session.joueur.checkInventaire('Pierre')} \n"
        f"Diamant : {Session.joueur.checkInventaire('Diamant')} \n"
        "\n"
        +Fore.GREEN + "-- Clés Donjons -- \n"+ Style.RESET_ALL +
        "\n"
        f"Facile: {Session.joueur.checkClé('Facile')} \n"
        f"Moyen: {Session.joueur.checkClé('Moyen')} \n"
        f"Difficile: {Session.joueur.checkClé('Difficile')} \n"
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
