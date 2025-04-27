#AYED
#5/09/24
van=int(input('Ingrese ancho: '))
val=int(input('Ingrese Altura: '))
vcaracter=input('Caracter: ')
def frectangulo(pa,pal,pcarac):
    if  van==1:
        for c in range(1,val+1):
            print(vcaracter, end='')
            print('')
    else:
        for c in range(1, val+1):
            print(vcaracter, end='')
        print('')
        if val!=1:
            for c in range(1, val-1):
                print(vcaracter, end='')
                for c in range(1, val-1):
                    print(' ',end='')
                print(vcaracter)
            for c in range(1, van+1):
                print(vcaracter, end='')
            print('')
#LO QUE ESTA MARCADO CON = ES RELLENO 
#=================================================================================================================
def fmensajeError(pan,pal):
    vlado = ''
    vladomsg = ''
    if van <=0:
        vlado += 'ancho'
        vladomsg += 'ancho: ' + str(van)
    if vlado != '' and val <=0:
        vlado += ' y de alto: ' + str(val)
    elif val <=0:
        vlado = 'alto'
        vladomsg += 'alto: ' + str(val)
    print('A ingresado de ' + vladomsg)
    print('[El ' + vlado + 'debe ser mayor a 0]' if len(vlado) == 5 or len(vlado) == 4 else '[El ' + vlado + ' debe ser mayores a 0]')
#========================================================================================================================================
if val > 0 and van > 0:
    frectangulo(van, val, vcaracter)
#else:
    #fmensajeError(van, val)
        