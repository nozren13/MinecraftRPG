from colorama import Fore, Style, init
from Instance.session import Session

init()

def menu_equipement():
    print(
        Fore.GREEN + " -- Inventaire -- \n" + Style.RESET_ALL +
        "\n"
        f"Casque : {Session.joueur.checkEquipement('Casque', 'Type')} \n"
        f"Plastron : {Session.joueur.checkEquipement('Plastron', 'Type')} \n"
        f"Jambiére : {Session.joueur.checkEquipement('Jambiére', 'Type')} \n"
        f"Botte : {Session.joueur.checkEquipement('Botte', 'Type')} \n"
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

