import math
p=input()
i=0
n=len(p)
j=len(p)-1
lista=[]
for i in range(n):
    if p[i] == p[j]:
        lista.append(1)
    i+=1
    j-=1

    
if lista.count(1) == math.ceil(n/2):
    print("Si")
else:
    print("No")