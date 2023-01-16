minute=int(input("Entrez le nombre de minutes écoulés depuis le début du mois :"))
heure = minute //60
date = heure //24
print(f"Nous sommes au {date}e jour du mois en cours")