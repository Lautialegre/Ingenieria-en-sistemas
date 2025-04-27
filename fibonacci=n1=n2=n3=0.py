velementos=7
v=[0]*velementos
import random
for c in range(velementos):
    v[c]=random.randint(1,100)
for barrido in range(1,velementos):
    vultiea=velementos-barrido
    for ea in range(0,vultiea):
        es=ea+1
        if v[ea]>v[es]:
            vauxi=v[ea]
            v[ea]=v[es]
            v[es]=vauxi
for c in range(0,velementos):
    print(v[c])
