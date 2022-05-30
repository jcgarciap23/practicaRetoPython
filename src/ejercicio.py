from math import sqrt as raiz_cuadrada
from random import shuffle as desordenar_lista
import numpy as np

def encriptado(texto):

    #Variable que controla cuando la longitud del texto sea el cuadrado de un entero
    texto_es_valido = False

    #Validación que la longitud del texto sea el cuadrado de un entero
    while(texto_es_valido == False):

        #Obtenemos la longitud del texto
        longitud_texto = len(texto)

        #Se calcula la raíz cuadrada de la longitud del texto
        raiz_longitud = raiz_cuadrada(longitud_texto)

        #Si la raíz es un entero entonces el texto es válido, si no se le concatena '_' hasta que sea válido el texto
        if((raiz_longitud - round(raiz_longitud)) == 0):
            texto_es_valido = True
        else:
            texto += '_'
    
    #Convertimos el texto en una lista
    lista_texto = list(texto)

    #Hacemos una lista con los indices de la lista_texto
    lista_texto_indices = list(range(len(lista_texto)))

    #Se usa la función shuffle de random para desordenar la lista de los indices
    desordenar_lista(lista_texto_indices)

    #Declaramos una lista vacía llamada lista_texto_desordenada
    lista_texto_desordenada = list()

    #Rellenamos la lista_texto_desordenada con la lista del texto según el orden de la lista de los indices
    for indice in lista_texto_indices:
        lista_texto_desordenada.append(ord(lista_texto[indice]))

    #Calculamos las dimensiones de la matriz (FilaxColumna)
    dimensiones_matriz = int(raiz_cuadrada(longitud_texto))

    #Convertimos la lista_texto_desordenada en un npArray unidimensional
    matriz_encriptado = np.array(lista_texto_desordenada)

    #Convertimos npArray unidimensional en una matriz bidimensional
    matriz_encriptado = matriz_encriptado.reshape(dimensiones_matriz, dimensiones_matriz)

    #Se retorna el resultado, matriz con el texto encriptado y la clave con la lista de los indices desordenados
    return matriz_encriptado, lista_texto_indices


def desencriptado(matriz_encriptado, clave):

    #Convertimos la matriz bidimensional en una lista
    matriz_encriptado = matriz_encriptado.ravel().tolist()

    #Declaramos una variable que va a contener el mensaje descifrado
    mensaje_original = list()

    #Recorremos la clave y ordenamos el mensaje, se descifra y se almacena en mensaje_original
    for indice in range(len(clave)):
        indice_original = clave.index(indice)
        mensaje_original.append(chr(matriz_encriptado[indice_original]))
    
    #Eliminamos los '_' que se agregaron si así fue el caso
    if '_' in mensaje_original:
        for indice, element in reversed(list(enumerate(mensaje_original))):
            if element == '_':
                mensaje_original.pop(indice)
            else:
                break  
    
    #Convertimos el mensaje en una cadena de caracteres
    mensaje_original = "".join(mensaje_original)  

    #Retornamos el mensaje descifrado
    return mensaje_original


if __name__ == "__main__":
    texto = 'Today is Caturday!'
    #texto = 'Vuela la mariposa de flor en flor… '
    print(encriptado(texto))
    [matriz_encriptado, clave] = encriptado(texto)
    print(desencriptado(matriz_encriptado, clave))








