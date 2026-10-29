from Outils import chemin, json


class ProgressionMixin:
    def modifier_statistique(self, stat, quantite):
        self.Statistique[stat] = self.Statistique.get(stat, 0) + quantite
        self._sauvegarder_statistique()
        self._mettre_a_jour_progression(stat, quantite)

    def _mettre_a_jour_progression(self, statistique, quantite):
        for chemin_service, progression in (
            (chemin.ServiceChemin.QUETES, self.Quetes),
            (chemin.ServiceChemin.SUCCES, self.Succes),
        ):
            objectifs = json.lire_fichier(chemin_service)
            for identifiant, objectif in objectifs.items():
                if objectif.get("Statistique") != statistique:
                    continue

                etat = progression.setdefault(
                    identifiant, {"Progression": 0, "Reussi": False}
                )
                if etat["Reussi"]:
                    continue

                cible = objectif["Objectif"]
                etat["Progression"] = min(
                    cible, etat.get("Progression", 0) + quantite
                )
                if etat["Progression"] >= cible:
                    etat["Reussi"] = True
                    recompenses = objectif["Récompenses"]
                    self.ajoutRécompense(recompenses["Argent"], recompenses["Xp"])

                if chemin_service == chemin.ServiceChemin.QUETES:
                    self._sauvegarder_quete()
                else:
                    self._sauvegarder_succes()
