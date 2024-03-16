mat=[[2,3,4], [7,9,10], [12,13,14]]
list=[]
for linha in mat:
    for elemento in linha:
        if elemento %2==0:
            list.append(elemento)
print(list)