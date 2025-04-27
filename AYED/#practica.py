vele=6
class Tpila:
    cima=0
    datos=['']*vele
def inicializar(ppila):
    ppila.cima=-1
    return ppila
def pilavacia(ppila):
    if ppila.cima==-1:
        vauxi=True
    else:
        vauxi=False
    return vauxi
def pilallena(ppila):
    if ppila.cima==vele-1:
        vauxi=True
    else:
        vauxi=False
    return vauxi
def meter(ppila,pdato):
    if pilallena(ppila):
        print('La pila esta llena')
    else:
        ppila.cima=ppila.cima+1
        ppila.datos[ppila.cima]=pdato
def sacar(ppila):
    if pilavacia(ppila):
        print('Pila vacia')
    else:
        vdato=ppila.datos[ppila.cima]
        ppila.cima=ppila.cima-1
        print(vdato)
#PRG PPAL
pila=Tpila
inicializar(pila)
votro=''
while votro!='N':
    apel=input('Ingrese apellido: ')
    meter(pila,apel)
    votro=input('desea continuar? [Y/N]')
votro=''
while votro!='N':
    sacar(pila)
    votro=input('desea continuar? [Y/N]')