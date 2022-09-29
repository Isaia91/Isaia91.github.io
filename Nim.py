import random
N=int(input('Le nombre de tour'))
print (N)
i=0
j1=0
j2=0
print (j1,'and',j2)
while i<N:
    j1= random.randint(1,3)
    j2=4-j1
    N=N-4
    print ("pick1:",j1,'et pick2:',j2)