import random

vnume=cpar=cimpar=0
vmayorpar=vmayorimp=vmenorpar=vmenorimp=0
c=acupar=acuimpar=0
prompar=promimp=0.0
vmayorauxpar=vmayorauximp=-9999999
vmenorparaux=vmenorimpaux=10000000
vmayorpar=vamorimp=vmenorpar=vmenorimp=0
acupar=acuimpar=0
for c in range(1,5000+1):
    vnume=random.randint(50,100)
    if vnume%2==0:
        cpar=cpar+1
        acupar=acupar+vnume
        if vnume>=vmayorauxpar:
            if vnume==vmayorauxpar:
                vmayorpar=vmayorpar+1
            else:
                vmayorauxpar=vnume
                vmayorpar=1
        if vnume<vmenorparaux:
            vmenorpar=vnume
    else:
        cimpar=cimpar+1
        acuimpar=acuimpar+vnume
        if vnume>=vmayorauximp:
            if vnume==vmayorauximp:
                vmayorimp=vmayorimp+1
            else:
                vmayorauximp=vnume
                vmayorimp=1
        if vnume<vmenorimpaux:
                vmenorimp=vnume
prompar=acupar/cpar
promimp=acuimpar/cimpar
print(vmayorpar)
print(vmayorimp)
print(prompar)
print(promimp)
print(vmenorpar)
print(vmenorimp)
