from colorama import Fore, Style, init

init()

class PrixMixin:
    def afficher_prix_objet(self, objets):
        while(True):
            print(
                Fore.GREEN + f" -- Achat/{objets} -- " + Style.RESET_ALL +
                "\n"
                )