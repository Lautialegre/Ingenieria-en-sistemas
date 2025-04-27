#AYED
#AUTOR LAUTY
import random
vele=5
v=[0]*vele
for c in range(0,vele):
    v[c]=random.randint(0,100)
ef=0
for barrido in range(0,vele):
    for ev in range(ef+1,vele):
        if v[ef]>v[ev]:
            vauxi=v[ef]
            v[ef]=v[ev]
            v[ev]=vauxi
    ef=ef+1
for c in range(0,vele):
    print(v[c])