def checkdata(start, end):
    if start<0 or start>24 or end<0 or end>24:
        print("Les horaires doivent etre entre 0 et 24 ")
        return False
    if start==end:
        print("Il ne ,peut pas y avoir moins d'une heure de location")
        return False
    if start>end:
        print("Le debut ne peut etre supérieur a la fin ")
        return False
    return True

def velo():
    start = int(input("Veuillez donner l'heure de debut de la location : "))
    end = int(input("veuillez donner l'heure de fin de la location : "))
    while not checkdata(start, end):
        start = int(input("Veuillez donner l'heure de debut de la location : "))
        end = int(input("veuillez donner l'heure de fin de la location : "))

    high=0
    low=0

    if end<7:
        low = end - start
    else:
        if start<7:
            low = 7 - start
            start = 7

        if end<17:
            high=2*(end-start)
        else:
            if start<17:
                high=2*(17-start)
                start=17
            low+=end-start

    print("vous avez loué votre vélo pendant ")
    if low>0:
        print(low, "heures a un tarif de 1 euro")
    if high>0:
        print(high//2, "heures a un tarif de 2 euros")
    print("Le prix  total de la location est de ", float(high+low), "euro(s).")

velo()