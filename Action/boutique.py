from Instance.session import Session
from Action.BoutiqueMixin.acheter import AcheterMixin
from Action.BoutiqueMixin.vendre import VendreMixin
from Models.item import Item


class Boutique(AcheterMixin, VendreMixin):
    def __init__(self):
        self.Joueur = Session.joueur
        self.Items = Item()

    def _demander_entier(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Merci de saisir un nombre entier.")

    def menu(self):
        while True:
            print(
                "\n-- Boutique --\n"
                "1 - Acheter\n"
                "2 - Vendre des ressources\n"
                "3 - Retour\n"
            )
            try:
                option = int(input("Quelle action voulez-vous faire (1 à 3) ? "))
            except ValueError:
                print("Merci de saisir un nombre entier.")
                continue

            if option == 1:
                self.acheter()
            elif option == 2:
                self.vendre()
            elif option == 3:
                return
            else:
                print("Choix invalide.")