class AjoutRécompenseMixin:
    XP_PAR_NIVEAU = 100

    def xp_requis_niveau_suivant(self):
        return max(1, self.Compte.get("Niveau", 1)) * self.XP_PAR_NIVEAU

    def _ajouter_xp(self, xp):
        ancien_niveau = self.Compte.get("Niveau", 1)
        ancien_xp = self.Compte.get("Xp", 0)
        self.Compte["Niveau"] = max(1, ancien_niveau)
        self.Compte["Xp"] = ancien_xp + xp
        niveaux_gagnes = 0

        while self.Compte["Xp"] >= self.xp_requis_niveau_suivant():
            self.Compte["Xp"] -= self.xp_requis_niveau_suivant()
            self.Compte["Niveau"] += 1
            niveaux_gagnes += 1

        if self.Compte["Niveau"] != ancien_niveau or self.Compte["Xp"] != ancien_xp:
            self._sauvegarder_Compte()
        return niveaux_gagnes

    def ajoutRécompense(self, argent, xp):
        argentAjouter = self.checkCompte("Argent") + argent
        self.modifier_Compte("Argent", argentAjouter)

        niveaux_gagnes = self._ajouter_xp(xp)
        if niveaux_gagnes:
            print(
                f"Félicitations ! Vous avez gagné {niveaux_gagnes} niveau(x). "
                f"Vous êtes maintenant niveau {self.Compte['Niveau']}."
            )
        