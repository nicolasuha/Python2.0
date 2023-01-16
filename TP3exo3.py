import random
passage = 1

M = random.randint(0, 100)
#print(M) pour voir le numéro tiré au hasard
N = int(input("Entrer un nombre : "))

while not(N == M):
    if N > M:
        print("Le nombre est trop grand")
        passage += 1
    else:
        print("Le nombre est trop petit")
        passage += 1
    N = int(input("Entrer un nombre : "))

print(f"Gagné ! Vous avez trouver le nombre mystère {M} en {passage} passage(s)")