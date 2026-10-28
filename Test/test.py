import time

debut = time.perf_counter()
fin =  debut + 5.0

while True:
    maintenant = time.perf_counter()
    restant = fin - maintenant

    if restant <= 0:
        print("\rTerminer!")
        break

    secondes = int(restant)
    millisecondes = int((restant-secondes)*1000)
    print(f"\r{secondes}.{millisecondes}", end="")
