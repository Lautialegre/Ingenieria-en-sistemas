def contar_consonantes(frase):
    contador=0
    for i in range(0,len(frase)):
         caracter=frase[i]
         asciivalor=ord(caracter)
         if (65<=asciivalor<=90 or 97 <= asciivalor <= 122):
             caracterminuscula=caracter.lower()
             
             if caracterminuscula != 'a' and caracterminuscula != 'e' and caracterminuscula != 'i' and caracterminuscula != 'o' and caracterminuscula != 'u':
                 contador += 1
    return contador

#PPAL
frase=input('Ingresa una frase: ')
cantidadconsonantes= contar_consonantes(frase)
print('La frase tiene: ',cantidadconsonantes,'consonantes')

        
