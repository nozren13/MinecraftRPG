from Models.joueur import *
from colorama import Fore, Style, init
from Instance.session import Session
from Menu.menu_jouer import menu_jouer

init()

def creation_compte():
    while(True):
        Email = input("Quelle est votre Email : ")
        Mdp = input("Quelle est votre Mots de passe : ")
        print("\n")

        if(Joueur.verifierJoueur(Email,Mdp)):
            Joueur.creationJoueur(Email, Mdp)
            Session.setJoueur(Email)
            menu_jouer()
        else:
            print(Fore.RED + "Un compte est déja crée sous ce nom\n"+"\n" + Style.RESET_ALL)
            

def connexion():
    tentative = 3
    while(tentative != 0):
        
        Email =input("Quelle est votre Email : ")
        Mdp = input("Quelle est votre Mots de passe : ")
        print("\n")
        if(Joueur.verifierJoueur(Email, Mdp)):
            print(Fore.LIGHTRED_EX +"Adresse ou Mdp invalide, Merci de réesayer.\n" + Style.RESET_ALL)
            tentative -= 1
            continue
                

        print(Fore.LIGHTGREEN_EX + "Connexion réussi ! \n" + Style.RESET_ALL + "\n")
        Session.setJoueur(Email)

        menu_jouer()

