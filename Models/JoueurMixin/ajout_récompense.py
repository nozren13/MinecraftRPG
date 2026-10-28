class AjoutRécompenseMixin :

    def ajoutRécompense(self, argent, xp):
        # Argent
        argentAjouter = self.checkCompte("Argent") + argent
        self.modifier_Compte("Argent", argentAjouter)

        # Xp
        xpAjouter = self.checkCompte("Xp") + xp
        self.modifier_Compte("Xp", xpAjouter)
        