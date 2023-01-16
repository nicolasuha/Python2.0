L1 = [0]*3
print(f"La liste {L1} le type {type(L1)} et l'id {id(L1)}")
for i in L1:
    print(f"la liste {i} le type {type(i)} et l'id {id(i)}")
L1[1] += 1
print ("aprés la modif")
print(f"la liste {L1} le type {type(L1)} et l'id {id(L1)}")
for i in L1:
    print(f"la liste {i} le type {type(i)} et l'id {id(i)}")
