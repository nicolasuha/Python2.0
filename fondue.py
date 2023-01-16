# Initialisation
BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

# Entrée utilisateur
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

# Calcul de la nouvelle quantitée
nouvelleQuantiteFromage = fromage * nbConvives / BASE
nouvelleQuantiteEau = eau * nbConvives / BASE
nouvelleQuantiteAil = ail * nbConvives / BASE
nouvelleQuantitePain = pain * nbConvives / BASE

# Sortie
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {nouvelleQuantiteFromage} gr de fromage")
print(f"- {nouvelleQuantiteEau} dl d'eau")
print(f"- {nouvelleQuantiteAil} grousse(s) d'ail")
print(f"- {nouvelleQuantitePain} gr de pain")
