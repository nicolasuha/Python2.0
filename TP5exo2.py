import sys

listenote = []
note = []
coef = []
notetotal = 0
coeftotal = 0

for i in range(0, 5):
    S1 = input(f"Veuillez entrer la note {i+1} du module 1 et le coefficient correspondant : ")
    S2 = S1.split(" ")
    if float(S2[0]) < 8:
        print("L'étudiant à une de ses notes inférieure à 8, il n'est donc pas admis")
        sys.exit()
    else:
        note.append(S2[0])
        coef.append(S2[1])

for j in range(0, 5):
    notetotal += float(note[j]) * float(coef[j])
    coeftotal += float(coef[j])

moyenne = notetotal / coeftotal

if moyenne < 10:
    print(f"L'étudiant à une moyenne générale inférieure à 10 ({moyenne}), il n'est donc pas admis")
else:
    print(f"L'étudiant est admis avec une moyenne de {moyenne}")