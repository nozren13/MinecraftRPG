# MinecraftRPG

MinecraftRPG est un jeu de rôle en ligne de commande, écrit en Python. Il permet de créer un compte, de récolter des ressources, de combattre des monstres et de faire progresser son personnage.

## Installation

Le projet utilise Python et la bibliothèque `colorama`.

1. Installez Python.
2. Installez la dépendance :

   python -m pip install colorama
   

3. Depuis le dossier du projet, lancez le jeu :

   python main.py
   

## Jouer

Depuis le menu d’accueil, créez un compte ou connectez-vous. Une fois connecté, le menu du jeu propose :

| Choix | Action |
| 1 | Consulter le profil |
| 2 | Consulter l’inventaire |
| 3 | Récolter du bois, de la pierre ou des diamants |
| 4 | Combattre un zombie, un squelette ou un creeper |
| 5 | Consulter les statistiques |
| 6 | Ouvrir la boutique |
| 7 | Consulter les quêtes |
| 8 | Consulter les succès |

Les menus attendent des choix numériques. Dans la boutique, choisissez l’achat ou la vente, puis suivez les indications affichées. Les achats sont payés avec l’argent du compte ; les ventes concernent le bois, la pierre et les diamants de l’inventaire.

## Expérience et niveaux

Les combats, les quêtes et les succès peuvent donner de l’expérience. Le premier niveau demande 100 XP, le suivant 200 XP, puis le seuil augmente de 100 XP à chaque niveau. L’XP en surplus est conservée. Le profil affiche l’XP actuelle et le seuil du prochain niveau.

Les données de compte et de progression sont enregistrées dans les fichiers JSON de `Data/Joueur`. Les articles et les objectifs des quêtes et succès sont définis dans `Data/Item` et `Data/Services`.

## Organisation du projet

- `Action/` : actions de jeu et logique de la boutique, du minage et des combats.
- `Menu/` : menus en ligne de commande.
- `Models/` : modèles du joueur, des objets et des entités.
- `Data/` : données JSON du jeu et sauvegardes des joueurs.
- `Instance/` et `Outils/` : session active, chemins de données et utilitaires.
