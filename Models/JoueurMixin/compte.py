from Outils import json, chemin

class JoueurCompteMixin:

    # Compte
    def creationJoueur(Email, Mdp):
        # Lire / récuperer Models
        donneesModels = json.lire_fichier(chemin.JoueurChemin.MODEL)
        cheminDonnees = [chemin.JoueurChemin.COMPTE, chemin.JoueurChemin.INVENTAIRE, chemin.JoueurChemin.STATISTIQUE , chemin.JoueurChemin.OUTILS, chemin.JoueurChemin.EQUIPEMENT, chemin.JoueurChemin.SUCCES, chemin.JoueurChemin.QUETES]
        sessionsModels = ["Compte", "Inventaire","Statistique", "Outils", "Equipement", "Succes", "Quetes"]

        for i, (cheminFichier, session)  in enumerate(zip(cheminDonnees, sessionsModels)) :
            donneesJoueur = json.lire_fichier(cheminFichier)

            donneesJoueur[Email] = donneesModels[session]

            # Modification
            if(session == "Compte"):
                donneesJoueur[Email]["Email"] = Email
                donneesJoueur[Email]["Mdp"] = Mdp

            # Enregistre
            json.enregistrer_donnees(cheminFichier, donneesJoueur) 

    def verifierJoueur(Email, Mdp):
        # Lire base de donnée
        donnees = json.lire_fichier(chemin.JoueurChemin.COMPTE)

        #Vérification
        if Email not in donnees:
            return True

        if donnees[Email]['Mdp'] != Mdp:
            return True

        return False
