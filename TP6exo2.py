def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
lst1 = [0, 1, 2]
lst2 = ajouter_elt(lst1, len(lst1))

print(lst1)
print(type(lst1))
print(id(lst1))

print(lst2)
print(type(lst2))
print(id(lst2))

#print(f"la liste {lst1} le type {type(lst1)} et l'id {id(lst1)}")
#print(f"la liste {lst2} le type {type(lst2)} et l'id {id(lst2)}")