#PROGRAMA DE ALTAS
varchisocio=open('socios.py','r')
vregistro=varchisocio.readline()
while vregistro!='':
    vector=vregistro.split(';')
    print(vector[0])
    print(vector[1])
    print(vector[2])
    print(vector[3])
    print(len(vector[4]))
    vregistro=varchisocio.readline()
varchisocio.close()