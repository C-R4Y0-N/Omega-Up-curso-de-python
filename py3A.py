i=0
lista = []
n=int(input())
for i in range(n):
    lista.append(int(input()))
    i+=1

lista.sort()
i=0
bandera=True
for i in range(n):
    y=lista.count(lista[i])
    if bandera==False:
        bandera=True
    else:
        if y == 1:
         print(lista[i],lista.count(lista[i]))
    
        if y == 2:
         print(lista[i],lista.count(lista[i]))
         bandera=False
    i+=1
       