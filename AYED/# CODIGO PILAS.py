# CODIGO PILAS 
#AYED
#AUTOR
#12/11/24
velementos=5
class Tpila:
    cima=0
    datos=['']*velementos
def pilavacia(ppila):
    if ppila.cima == -1:
        vauxi= True
    else:
        vauxi=False
    return vauxi  #RETORNAR SIEMPRE VAUXI SINO NO VA A RECONOCER CUANDO ESTA VACIA, NI LLENA
def inicializar(ppila):
    ppila.cima=-1
    return ppila
def pilallena(ppila):
    if ppila.cima ==velementos-1:
        vauxi=True
    else:
        vauxi=False
    return vauxi
def meter(ppila,pdato):
    if pilallena(ppila):
        print('pila llena')
    else:
        ppila.cima=ppila.cima+1
        ppila.datos[ppila.cima]=pdato
def sacar(ppila):
    if pilavacia(ppila):
        print('pila vacia')
    else:
        vdato=ppila.datos[ppila.cima]
        ppila.cima=ppila.cima -1
        print(vdato)
    return ppila
#PRG PPAL 
pila = Tpila
inicializar(pila)
votro='' 
while votro!='n':
    vape=input('apellido')
    meter(pila,vape)
    votro=input('desea continuar? ')
votro = '' #REINICIAR VOTRO LUEGO DE CADA CICLO WHILE [SACAR/METER]
while votro !='n':
    sacar(pila)
    votro=input('sacar otro ?')
    

