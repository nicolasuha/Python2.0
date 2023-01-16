x = int(input(" Entrez un nombre entier : "))
if x%2 == 0:
    print("pair")
else:
    print("impair")

if x > 0 :
    print("Le nombre est positif")
elif x < 0 :
    print("Le nombre est négatif")
else :
    print("Le nombre est zéro ( et il est pair )")