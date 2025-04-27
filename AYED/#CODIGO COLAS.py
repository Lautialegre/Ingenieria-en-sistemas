#CODIGO COLAS 
#AYED 
#AUTOR
vele=5
class Tcola:
    frente=0
    final=0
    datos=[0]*vele
def inicializarcola(pcola):
    pcola.frente=0
    pcola.final=0
    return
def colavacia(pcola):
    if pcola.frente==pcola.final:
        vauxi=True
    else:
        vauxi=False
    return vauxi 
def colallena(pcola):
    vsiguiente = (pcola.final+1)%vele
    if vsiguiente==pcola.frente:
        vauxi=True
    else:
        vauxi=False
    return vauxi
def meter(pcola,pdatos):
    if colallena(pcola):
        print('Dato no ingresado cola llena')
    else:
        pcola.datos[pcola.final]=pdatos
        pcola.final= (pcola.final + 1)%vele
def sacar(pcola):
    if pcola.frente == pcola.final:
        print('No hay datos cola vacia')
    else:
        vdato=pcola.datos[pcola.frente]
        pcola.frente= (pcola.frente + 1)%vele
        print(vdato)
#PRG PPAL
cola=Tcola
votro=''
inicializarcola(cola)
while votro!='n':
    vnro=int(input('nro'))
    meter(cola,vnro)
    votro=input('desea continuar?')
votro=''
while votro!='n':
    sacar(cola)
    votro=input('sacar otro? ')

    