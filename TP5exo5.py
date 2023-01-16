heure=int(input("Entrez le nombre d'heures de travail : "))
if heure<161:
    y=heure*1
    print("vous n'avez pas dépassé les 160, vous êtes à", [y], "heures donc le salaire reste normal");
if heure>160 and heure<201:
    y=(heure-160)*1.25
    z=(heure-160)
    print("vous avez travaillé" , [heure], "heures, donc");
    print("vous avez travaillé", [z], "heures en plus des 160 heures");
    print(z, "*1.25 =", [y]);
if heure>200:
    y=(heure-160)*1.5
    z=(heure-160)
    print("vous avez travaillé" , [heure], "heures, donc");
    print("vous avez travaillé", [z], "heures en plus des 160 heures");
    print(z, "*1.5 =", [y]);