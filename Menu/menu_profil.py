from colorama import Fore, Style, init
from Instance.session import Session

init()
def menu_profil():

    print(
        Fore.GREEN + " -- Profil -- \n" + Style.RESET_ALL +
        "\n"
        f"Nom : {Session.joueur.Email} \n"
        f"Argent : {Session.joueur.checkCompte('Argent')} \n"
        f"Vie : {Session.joueur.checkCompte('Vie')}\n"
        f"Niveau : {Session.joueur.checkCompte('Niveau')}\n"
        f"Xp : {Session.joueur.checkCompte('Xp')}/"
        f"{Session.joueur.xp_requis_niveau_suivant()} pour le niveau suivant\n"
        "\n"
    )
