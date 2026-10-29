from Outils import chemin, json
from colorama import Fore, Style, init

init()

class JoueurProfilMixin:
    def getCompte(self) :
        print(
            Fore.BLUE + "---Information Compte---\n" + Style.RESET_ALL +
            "\n"
            f"Email : {self.Email}\n"
            f"Mdp : {self.Compte['Mdp']} \n"
            f"Argent : {self.Compte['Argent']}\n"
            f"Vie : {self.Compte['Vie']}\n"
            f"Niveau : {self.Compte['Niveau']}\n"
            f"Xp : {self.Compte['Xp']} \n"
        )

    def getInventaire(self):
        print(
            Fore.BLUE + "---Inventaire---\n" + Style.RESET_ALL +
            "\n"
            "-Matériaux-\n"
            "\n"
            f"Bois : {self.Inventaire['Bois']}\n"
            f"Pierre : {self.Inventaire['Pierre']}\n"
            f"Diamant : {self.Inventaire['Diamant']}\n"
            "\n"
            "-Clé donjon- \n"
            "\n"
            f"Facile : {self.Inventaire['Clé_Donjon']['Facile']}\n"
            f"Moyen : {self.Inventaire['Clé_Donjon']['Moyen']}\n"
            f"Difficile : {self.Inventaire['Clé_Donjon']['Difficile']}\n"
            "\n"
        )

    def getStatistique(self):
        print(
            Fore.BLUE + "---Statistique--- \n" + Style.RESET_ALL +
            "\n"
            "-Total de Mobs tuer- \n"
            "\n"
            f"Zombie : {self.Statistique['Zombie']} \n"
            f"Squelette : {self.Statistique['Squelette']}\n"
            f"Creeper : {self.Statistique['Creeper']}\n"
            "\n"
            "-Métériaux récuperer-\n"
            "\n"
            f"Bois : {self.Statistique['Bois']}\n"
            f"Pierre : {self.Statistique['Pierre']}\n"
            f"Diamant : {self.Statistique['Diamant']}\n"
            "\n"
            )

    def getEquipement(self):
        print(
            Fore.BLUE + "---Equipement--- \n" + Style.RESET_ALL +
            "\n"
            "-Equipement-\n"
            "\n"
            f"Casque : {self.Equipement['Casque']}\n"
            f"Plastron : {self.Equipement['Plastron']}\n"
            f"Jambiére : {self.Equipement['Jambiére']}\n"
            f"Botte : {self.Equipement['Botte']}\n"
            "\n"
            "-Outils-\n"
            "\n"
            f"Epee : {self.Outils['Epee']}\n"
            f"Hache : {self.Outils['Hache']}\n"
            f"Pioche : {self.Outils['Pioche']}\n"
            f"Potion : {self.Outils['Potion']}\n"
            "\n"
            )

    def getSucces(self):

        donneesSucces = json.lire_fichier(chemin.ServiceChemin.SUCCES)

        print(Fore.BLUE + "---Succes--- \n" + Style.RESET_ALL +"\n")
        
        for clé, succes in donneesSucces.items():
            etat = self.Succes.get(clé, {"Progression": 0, "Reussi": False})
            print(
                f"{succes['Titre']} : \n"
                f" - Objectif : {succes['Objectif']} \n"
                f" - Récompenses : {succes['Récompenses']['Argent']}€ / {succes['Récompenses']['Xp']} xp\n"
                f" - Progression : {etat['Progression']}/{succes['Objectif']} \n"
                f" - Réussi : {etat['Reussi']} \n"
                "\n"
            )

    def getQuetes(self):

        donnesQuetes = json.lire_fichier(chemin.ServiceChemin.QUETES)

        print(Fore.BLUE + "---Quêtes--- \n" + Style.RESET_ALL + "\n")
        for clé, quetes in donnesQuetes.items():
            etat = self.Quetes.get(clé, {"Progression": 0, "Reussi": False})
            print(
                f"{quetes['Titre']} : \n"
                f" - Objectif : {quetes['Objectif']} \n"
                f" - Récompenses : {quetes['Récompenses']['Argent']}€ / {quetes['Récompenses']['Xp']} xp\n"
                f" - Progression : {etat['Progression']}/{quetes['Objectif']} \n"
                f" - Réussi : {etat['Reussi']} \n"
                "\n"
            )