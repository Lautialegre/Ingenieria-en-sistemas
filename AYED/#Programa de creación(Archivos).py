#Programa de creación 
varchisocio=open('socios.txt','w')
votro=''
while votro!='n':
    vnrosocio=int(input('Ingrese numero de socio: '))
    vapel=input('Ingrese apellidos: ')
    valtu=float(input('Ingrese altura: '))
    vedad=int(input('Ingrese edad: '))
    vdepor= input('B para basquet, V para voley, F para futbol')
    vregistro=str(vnrosocio)+ ';' + vapel + ';' + str(vedad) + ';' + vdepor
    varchisocio.write(vregistro)
    varchisocio.write('\n')
    votro=input('Desea ingresar otro socio? [s/n]')
varchisocio.close()
