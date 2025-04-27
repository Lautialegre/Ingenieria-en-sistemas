#AYED
#AUTOR LAUTY
#13/8/24
velementos=5
vector=['']*velementos
vregistro=input('ingresar datos: ')
vlargo=len(vregistro)
x=0
e=0
while x<vlargo:
    if vregistro[x]==';':
        e=e+1
    else:
        vector[e]=vector[e]+vregistro[x]
    x=x+1
for e in range(0,velementos):
    print(vector[e])