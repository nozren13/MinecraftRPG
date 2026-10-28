from colorama import Fore, Style, init

init

def boutique():
    while(True):
        print(
            Fore.GREEN + " -- Boutique -- \n" + Style.RESET_ALL +
            "\n"
            "1 - Acheter \n"
            "2 - Vendre \n"
            "3 - Retour \n"
            "\n"
        )

        try:
            option = int(input("Quelle action voulez-vous faire(1 à 4) : "))
            print("\n")
        except ValueError:
            print(Fore.RED + "Erreur. Merci de donnez un chiffre \n" + Style.RESET_ALL)
            continue