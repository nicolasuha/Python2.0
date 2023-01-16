# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

jour = int(input("Entrez le nombre de jours : "))
heure = int(input("Entrez le nombre d'heures : "))
minute = int(input("Entrez le nombre de minutes : "))
heure_ecoule = heure + (jour * 24)
minute_ecoule = minute + (heure_ecoule * 60)
print("Le nombre de minutes écoulées est de ", minute_ecoule)
