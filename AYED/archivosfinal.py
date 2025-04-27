#AYED
#AUTOR LAUTY
varchi=open('deportistas.dat','r')
vregistro=varchi.readline().rstrip()
vector=vregistro.split('#')
zmax=0
while vregistro!='':
    dni=int(vector[0])
    apellido=vector[1]
    altura=float(vector[2])
    peso=float(vector[3])
    deporte=vector[4]
    z=0
    acualtu=0
    dnimax=0
    vcontrol=deporte
    while vregistro!='' and vcontrol==deporte:
        z=z+1
        acualtu=acualtu+altura
        if dni>dnimax:
            dnimax=dni
        vregistro=varchi.readline().rstrip()
        if vregistro!='':
            vector=vregistro.split('#')
            dni=int(vector[0])
            apellido=vector[1]
            altura=float(vector[2])
            peso=float(vector[3])
            deporte=vector[4]
    prom=acualtu/z
    print(z,dnimax,prom,vcontrol)
    if z>zmax:
        zmax=z
        depomax=vcontrol
print(depomax,zmax)
varchi.close()