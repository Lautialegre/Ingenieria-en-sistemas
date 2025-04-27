#EJERCICIO CORTE DE CONTROL ARCHIVOS FINAL
#EJERCICIO 2:Código en Python.Corte de control doble ciclo mientras. (EN PAPEL) 
#Se tiene el siguiente archivo plano que contiene los datos de los socios de un club, la estructura es la siguiente :
#Registro :
# nrosocio entero 
# apellido cadena 
# categoria cadena
# ciudad cadena 
# edad entero 
#separador: ';'
# la categoria es una letra A, B o C
# El archivo esta ordenado por el campo ciudad 
#Mostrar:
#Cantidad de socios que viven en cada ciudad 
#Cantidad de socios de categoria A en cada ciudad 
#Promedio de edad por cada ciudad 
#Nombre de la ciudad en la que viven mayor cantidad de socios (máximo no repetido)
varchi=open('datos.dat','r')
vregistro=varchi.readline().rstrip()
vector=vregistro.split(';')
zmax=0
while vregistro!='':
    nrosocio=int(vector[0])
    vapel=vector[1]
    vcate=vector[2]
    vciudad=vector[3]
    vedad=int(vector[4])
    vcontrol=vciudad
    z=za=0
    acuedad=0
    while vcontrol==vciudad and vregistro!='':
        z+=1
        acuedad=acuedad+vedad
        if vcate == 'A':
            za+=1
        vregistro=varchi.readline().rstrp()
        if vregistro!='':
            nrosocio=int(vector[0])
            vapel=vector[1]
            vcate=vector[2]
            vciudad=vector[3]
            vedad=int(vector[4])
    vprom=acuedad/z
    print(z,za,vprom,vcontrol)
    if z>vmax:
        vmax=z
        vciumax=vcontrol
print('La ciudad con mayor cantidad de socios es:  ', vciumax, 'con: ', zmax,'socios')
varchi.close()
        
    
        


