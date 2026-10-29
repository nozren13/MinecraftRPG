from copy import deepcopy

from colorama import Fore, Style


class AcheterMixin:
    def acheter(self):
        articles = []
        for categorie, donnees in self.Items.Outils.items():
            for type_item, details in donnees.items():
                if type_item:
                    articles.append((f"{categorie} en {type_item}", "outil", categorie, type_item, details))

        for categorie, donnees in self.Items.Equipement.items():
            for type_item, details in donnees.items():
                if type_item:
                    articles.append((f"{categorie} en {type_item}", "equipement", categorie, type_item, details))

        potion = self.Items.Nourriture["Potion"]["Regeneration"]
        articles.append(("Potion de régénération", "potion", "Potion", 1, potion))

        while True:
            print(Fore.GREEN + "-- Articles disponibles --" + Style.RESET_ALL)
            for index, (nom, _, _, _, details) in enumerate(articles, start=1):
                print(f"{index} - {nom} : {details['Prix']} pièces")
            print("0 - Retour\n")

            choix = self._demander_entier("Quel article voulez-vous acheter ? ")
            if choix == 0:
                return
            if choix < 1 or choix > len(articles):
                print(Fore.RED + "Choix invalide.\n" + Style.RESET_ALL)
                continue

            nom, type_article, categorie, type_item, details = articles[choix - 1]
            quantite = 1
            if type_article == "potion":
                quantite = self._demander_entier("Combien de potions voulez-vous acheter ? ")
                if quantite <= 0:
                    print(Fore.RED + "La quantité doit être supérieure à zéro.\n" + Style.RESET_ALL)
                    continue

            prix = details["Prix"] * quantite
            if self.Joueur.checkCompte("Argent") < prix:
                print(Fore.RED + "Vous n'avez pas assez d'argent.\n" + Style.RESET_ALL)
                continue

            article_achete = {
                cle: valeur for cle, valeur in details.items() if cle != "Prix"
            }
            self.Joueur.modifier_Compte("Argent", self.Joueur.checkCompte("Argent") - prix)
            if type_article == "outil":
                self.Joueur.modifier_outil(categorie, deepcopy(article_achete))
            elif type_article == "equipement":
                equipement = deepcopy(article_achete)
                equipement["Type"] = type_item
                self.Joueur.modifier_equipement(categorie, equipement)
            else:
                self.Joueur.modifier_outil("Potion", type=quantite)

            print(Fore.GREEN + f"Achat effectué : {nom} (prix : {prix} pièces).\n" + Style.RESET_ALL)