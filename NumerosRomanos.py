import re

dic_numeros = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }


def eval_romano(numero):
    """
    Esta funcion comprueba que se cumplen todas las condiciones para que un numero romano sea valido. Si No es valido devolvera False, en caso 
    contrario devolvera True
    """

    if(re.search("VX|VL|VC|VD|VM|LC|LD|LM|DM",numero)):#Los símbolos 5 y sus múltiplos (V, L, D) siempre suman y no pueden estar a la izquierda de uno de mayor valor.
        return False
    elif(re.search("IC|IM|IL|ID|XD|XM",numero)):#Solo se puede restar un símbolo de tipo 1 (I, X, C, M) sobre el inmediato mayor de tipo 1 o de tipo 5 (V, L, D).
                                                #El símbolo I solo puede restar a V y a X.    #X solo puede restar a L y a C.
        return False

    for item in numero:#Iteramos el numero introducido por consola
        if(re.search(item,"[IVXLCDM]") == None):#Recorre el numero y comprueba que todos los digitos esten en la cadena de numero romanos
            return False
        elif(re.search('%s{4,}'%item,numero))!= None:#Se permiten como mucho tres repeticiones consecutivas del mismo símbolo.
            return False
        
        evalua_repeticion_resta = (re.search('%s{2,}.'%item,numero))#Un símbolo que aparece restando solo se puede repetir cuando su repetición esté colocada a más de un símbolo de distancia a su derecha.
        if evalua_repeticion_resta:
            #obtenemos la letra de la posicion posterior a la coincidencia
            letra_posterior = numero[(re.search('%s{2,}.'%item,numero).span())[1]-1]
            #print(letra_posterior)#obtenemos la letra de la posicion posterior a la coincidencia    
            #print(item)
            #A continuacion debemos comprobar si el valor de la letra es mayor al valor del item
            if(dic_numeros[letra_posterior]>dic_numeros[item]):
                return False

    return True


def calculadora_rom_to_dec(numero):
    """
    Esta funcion convierte un numero romano a un numero decimal
    """
    resultado = 0
    temporal = 0

    for i in range(len(numero)-1,-1,-1):#recorremos el numero romano de derecha a izquierda
        if(dic_numeros[numero[i]]>=temporal):
            resultado += dic_numeros[numero[i]]
            temporal = dic_numeros[numero[i]]
        else:
    
            resultado -= dic_numeros[numero[i]]
            temporal = dic_numeros[numero[i]]
        
    return resultado

#REVISAR Y ANALIZAR FUNCION PARA CONVERTIRLA EN DICCIONARIO Y TRABAJAR CON EL 
def calculadora_dec_to_rom(numero_entero):
    """
    Esta funcion convierte un numero decimal a un numero romano
    """
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    resultado = ''
    i=0

    while numero_entero > 0:
        for _ in range(numero_entero // numeros[i]):
            resultado += numerales[i]
            numero_entero -= numeros[i]

        i += 1
    
    return resultado


def is_decimal(numero):
    try:
        numero = int(numero)
    except:
        return False
    return True



############################## EJECUCION DEL PROGRAMA   #########################

##########      CALCULA DECIMAL A ROMANO    ##########
"""
num_decimal = int(input("Introduce un numero entero positivo menor de 4000: "))

if(num_decimal < 4000):
    print(calculadora_dec_to_rom(num_decimal))
else:
    print("No se pueden representar numeros mayores a 3999")

"""


###########     CALCULA ROMANO A DECIMAL    ###########
"""
numero = input("Introduce el numero a calcular: ").upper()#Pasar a mayusculas

if(eval_romano(numero)):
    print(f"El valor de {numero} en decimal es : {calculadora_rom_to_dec(numero)} ")
else:
    print(f"{numero} no es un numero romano valido")

"""
