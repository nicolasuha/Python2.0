str = input("Nom 1 : ")
x = str.upper()

str1 = input("Prénom 1 : ")
x1 = str1.capitalize()

str2 = input("Nom 2 : ")
x2 = str2.upper()

str3 = input("Prénom 2 : ")
x3 = str3.capitalize()

list1 = [x, x2]     #ordre des noms
list2 = [x1, x3]    #ordre des prénoms

if list1 [0] < list1 [1]:
    print(f"{x, x1, x2, x3}")

elif list1 [1] < list1 [0]:
    print(f"{x2, x3, x, x1}")

else:
    if list2 [0] > list2 [1] :
        print(f"{x, x1, x2, x3}")
    else :
        print(f"{x2, x3, x, x1}")
