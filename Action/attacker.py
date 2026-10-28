from Action.AttackeMixin.protection import ProtectionMixin
from Action.AttackeMixin.soigne_joueur import SoigneJoueurMixin
from Action.AttackeMixin.attacke_joueur import AttackeJoueurMixin
from Action.AttackeMixin.attacke_mobs import AttackeMobsMixin
from Models.entite import Entite


class Attacker(ProtectionMixin, SoigneJoueurMixin, AttackeJoueurMixin, AttackeMobsMixin):

    def __init__(self, mobs):
        self.Mobs = Entite(mobs)