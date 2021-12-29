from NumerosRomanos import *

max_longitud = 0
lista =[]
for i in range(1,4000):
    if (len(calculadora_dec_to_rom(i))>max_longitud): 
        max_longitud = len(calculadora_dec_to_rom(i))
        lista.append((calculadora_dec_to_rom(i)))

print(lista)
print(max_longitud)
