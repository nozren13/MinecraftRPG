from colorama import Fore, Style, init

init()
class TourJoueurMixin:

    def tour_joueur(self):
        while(True):
            print(
                Fore.BLUE + "--Votre Tour--" + Style.RESET_ALL +
                "\n"
                "1 - Attacker \n"
                "2 - Soigner \n"
                "3 - Quitter le combats \n"
                "\n"
            )

            try:
                option = int(input("Quelle action voulez-vous faire(1 à 3) : "))
                print("\n")
            except ValueError:
                print(Fore.RED + "Erreur. Merci de donnez un chiffre \n"+"\n" + Style.RESET_ALL)
                continue
            
            if option == 1:
                if self.Joueur.joueur_attacker_mobs():   # le mob est mort
                    break
                if not self.tour_mobs():                 # le joueur est mort
                    break
            elif option == 2 :
                résultat = self.Joueur.soignerJoueur()
                if résultat:
                    continue
            elif option == 3 :
                print(Fore.CYAN+"Vous avez quitter le combats\n"+"\n"+Style.RESET_ALL )
                break
            else :
                print( Fore.RED+ "Donnez un chiffre entre 1 et 3.\n"+"\n"+Style.RESET_ALL)
