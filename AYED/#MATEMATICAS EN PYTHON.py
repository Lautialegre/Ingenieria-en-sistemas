#Para utilizar las funciones seno, coseno, etc  
import math 
valor=float(input('ingrese número a calcular: '))

#Para definir números complejos 
z1 = complex(2, 3) # 2 + 3i (parte real, parte imaginaria)
z2 = complex(1, -4) # 1 - 4i 
#Operaciones con estos números: 
suma = z1 + z2
resta = z1 - z2
producto = z1 * z2
cociente = z1 / z2
#Raíz cuadrada de un numero 
Número= math.sqrt(valor) 
#Ángulo en grados
angulo_grados = 30
#Pasar el ángulo a radianes
angulo_grados = math.radians(angulo_grados)
#Funciones trigonométricas 
seno = math.sin(valor)
coseno = math.cos(valor)
tangente = math.tan(valor)
#Funciones recíprocas
cosecante = 1/seno 
secante = 1/coseno
cotangente = 1/tangente
#Funciones trigonométricas inversas
arco_seno = math.degrees(math.asin(seno))
arco_coseno = math.degrees(math.acos(coseno))
arco_tangente = math.degrees(math.atan(tangente))
