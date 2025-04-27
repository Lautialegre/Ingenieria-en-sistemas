#AYED
#AUTOR LAUTY
#COLAS
#METODOS DE COLA:
#INICIALIZAR COLA
#COLA LLENA
#COLA VACIA
#METER O AGREGAR UN DATO
#SACAR UN DATO
vele=5
class Tcola:
    frente=0
    final=0
    datos=[0]*vele
def inicializar(pcola):
    pcola.frente=0
    pcola.final=0
def colavacia(pcola):
    if pcola.frente==pcola.final:
        vauxi=True
    else:
        vauxi=False
    return vauxi
def colallena(pcola):
    vsiguiente=(pcola.final+1)%vele
    if vsiguiente==pcola.frente:
        vauxi=True
    else:
        vauxi=False
    return vauxi
def meter(pcola,pdato):
    if colallena(pcola):
        print('La cola esta llena')
    else:
        pcola.datos[pcola.final]=pdato
        pcola.final=(pcola.final+1)%vele
def sacar(pcola):
    if pcola.frente==pcola.final:
        print('La cola esta vacia')
    else:
        vdato=pcola.datos[pcola.frente]
        pcola.frente=(pcola.frente+1)%vele
        print(vdato)
#PRG PPAL
cola=Tcola
inicializar(cola)
votro=''
while votro!='N':
    vnro=int(input('Ingrese Número: '))
    meter(cola,vnro)
    votro=input('Dese ingresar otro? [Y/N]')
votro=''
while votro!='N':
    sacar(cola)
    votro=input('Desea sacar otro? [Y/N]')