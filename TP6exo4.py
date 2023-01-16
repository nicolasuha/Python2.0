import random
nb = 100
print(f"Générer {random.randint(0, nb)} nombres entiers entre 0 et 100")
tab = random(nb, 0)
tab.sort()
print(tab)


