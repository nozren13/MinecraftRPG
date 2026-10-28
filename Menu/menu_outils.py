from colorama import Fore, Style, init
from Instance.session import Session

init()

def menu_outils():
    print(
        Fore.GREEN + " -- Outils -- \n" + Style.RESET_ALL +
        "\n"
        f"Epee : {Session.joueur.checkOutil('Epee', 'Type')} \n"
        f"Hache : {Session.joueur.checkOutil('Hache', 'Type')} \n"
        f"Pioche : {Session.joueur.checkOutil('Pioche', 'Type')} \n"
        f"Potion : {Session.joueur.checkPotion()} \n"
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
