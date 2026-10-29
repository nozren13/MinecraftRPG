from colorama import Fore, Style


class VendreMixin:
    PRIX_VENTE = {
        "Bois": 1,
        "Pierre": 2,
        "Diamant": 10,
    }

    def vendre(self):
        ressources = list(self.PRIX_VENTE.items())

        while True:
            print(Fore.GREEN + "-- Ressources rachetables --" + Style.RESET_ALL)
            for index, (nom, prix) in enumerate(ressources, start=1):
                print(f"{index} - {nom} : {prix} pièce(s) l'unité")
            print("0 - Retour\n")

            choix = self._demander_entier("Quelle ressource voulez-vous vendre ? ")
            if choix == 0:
                return
            if choix < 1 or choix > len(ressources):
                print(Fore.RED + "Choix invalide.\n" + Style.RESET_ALL)
                continue

            nom, prix_unitaire = ressources[choix - 1]
            quantite = self._demander_entier(f"Combien de {nom.lower()} voulez-vous vendre ? ")
            if quantite <= 0:
                print(Fore.RED + "La quantité doit être supérieure à zéro.\n" + Style.RESET_ALL)
                continue
            if self.Joueur.checkInventaire(nom) < quantite:
                print(Fore.RED + f"Vous ne possédez pas assez de {nom.lower()}.\n" + Style.RESET_ALL)
                continue

            total = prix_unitaire * quantite
            self.Joueur.modifier_inventaire(nom, -quantite)
            self.Joueur.modifier_Compte("Argent", self.Joueur.checkCompte("Argent") + total)
            print(Fore.GREEN + f"Vente effectuée : {quantite} {nom.lower()} pour {total} pièces.\n" + Style.RESET_ALL)
