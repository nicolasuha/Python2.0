a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

# permutation
temp = a
temp2 = b
b = temp
a = c
c = temp2

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)