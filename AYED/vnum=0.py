#AYED
#Autor Lauty
#10/09/24
nrosucursales = 15
totaltoneladas = [0]*nrosucursales
cantidadproduciones = [0]*nrosucursales
totaltoneladasmes=[0]*12
vmaxi=-99999999
def fprocesarproduccion():
    x=0
    while x==0:
        #ingreso de datos
        nrosucursal=int(input('Ingrese el numero de sucursal (1,15): '))
        toneladasproducidas=float(input('Ingrese las toneladas producidas: '))
        fechaproduccion= input('Ingrese la fecha de produccion (dd/mm/aaaa): ')
        if nrosucursal < 0 or nrosucursal >= nrosucursales:
            print('Numero de sucursal invalido. Debe estar entre 1 y 15')
        #Actualizar el total de toneladas y cantidad de producciones
        totaltoneladas[nrosucursal] += toneladasproducidas
        cantidadproduciones[nrosucursal]+=1
        #Validamos el formato de la fecha y extraemos el mes
        if len(fechaproduccion)==10 and fechaproduccion[2]== '/' and fechaproduccion[5] == '/':
             mes=int(fechaproduccion[3:5])
             if 1 <= mes <= 12:   
                 totaltoneladasmes[mes-1]+=toneladasproducidas
             else:
                 print('Mes invalido. Debe estar entre 1 y 12')     
        x=int(input('¿Desea continuar? (0 = SI/1 = No) : '))
def fmostrarresultados():
    for i in range(nrosucursales):
        if cantidadproduciones[i]>0:
            promedio=totaltoneladas[i]/cantidadproduciones[i]
            print('Sucursal', i + 1, ':')
            print('Total de toneladas producidas:', totaltoneladas[i])
            print('Cantidad de producciones', cantidadproduciones[i])
            print('Promedio de toneladas producidas:', promedio)
    #Encontrar el maximo total de toneladas producidas
    if nrosucursales > 0:
        maxtotal= totaltoneladas[0]
        for i in range(1, len(totaltoneladas)):
            if totaltoneladas[i] > maxtotal:
                maxtotal = totaltoneladas[i]
        sucursalesmaxtotal=0
        for i in range(len(totaltoneladas)):
            if totaltoneladas[i] == maxtotal:
                sucursalesmaxtotal+=1
        print('Numero de sucursales con el mayor total de toneladas producidas', maxtotal,':',sucursalesmaxtotal)
    print('Total de toneladas producidas por cada mes: ')
    for i in range(12):
        print('Mes', i+1, ':', totaltoneladasmes)
fprocesarproduccion()
fmostrarresultados()
        
        



        

