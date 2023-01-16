mode=int(input('Quel mode (0 = for, 1 = while) : '))
Nb=int(input('Entrez un entier naturel :' ))
a=1
y=1
if mode == 0:
    for i in range(1, Nb+1):
        a=a*i
    print(a)
else:
    while y!= Nb+1:
        a=a*y
        y+=1
        print(a)