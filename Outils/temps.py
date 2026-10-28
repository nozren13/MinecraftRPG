import threading
from Instance.session import Session
import time

def compte_a_rebours(seconde):

    debut = time.perf_counter()
    fin =  debut + seconde

    while True:
        maintenant = time.perf_counter()
        restant = fin - maintenant

        if restant <= 0:
            print("\n")
            return True

        secondes = int(restant)
        millisecondes = int((restant-secondes)*1000)
        print(f"\rTemps restants : {secondes}.{millisecondes}", end="")

def compte_a_rebours_Vie():

    debut = time.perf_counter()
    fin =  debut + 3600

    while True:
        maintenant = time.perf_counter()
        restant = fin - maintenant

        if restant <= 0:
            print("Votre vie a été remis a fond!\n")
            Session.joueur.modifier_Compte("Vie", 100)
            break

def arriére_plan_compte_a_rebours():
    thread_compte = threading.Thread(target=compte_a_rebours_Vie)
    thread_compte.start()
        