#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from dataclasses import replace
import operator
import sys
from collections import defaultdict
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    miDict = defaultdict(list)
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.replace("\n", "").strip().split("\t")
        val = val.split(",")

        for letra in val:
            miDict[letra].append(key)

        # for letra in val:
        #     if letra == ",":
        #         continue
        #     else:
        #         miDict[letra].append(key)
    
    sortedDict = sorted(miDict.items(), key=operator.itemgetter(0))
    #print(sortedDict)
    for k, v in sortedDict:
        # esta forma ordena calculando el largo de cada número y con base a esto ordena el número, es decir, ordena primero
        # todos los numeros de 0-9 y que tienen un largo de 1, despues los numeros de 11-99 y que tienen un largo de dos y
        # asi sucesivamente. Es más eficiente usar el lamda que la siguiente función.
        #res = sorted (v, key=lambda x:(len(x), x))
        # convierte en enetero mientras se realiza la función de ordenamiento
        res = sorted(v, key = int)
        # uno la lista por comas
        v = ",".join(map(str, res))

        sys.stdout.write("{}\t{}\n".format(k, v))


    # Con esta forma se une el diccionario con coma y se elimina la lista, pero necesitaba primero ordenar los valores de la 
    # lista, por eso no lo use.
    # for letra in miDict:
    #     miDict[letra] = ",".join(miDict[letra])

    # otra forma
    
        # for letra in val:
        #     if letra not in dicc:
        #         lista.append(int(key))
        #         dicc[letra] = lista
        #     elif letra in dicc:
        #         lista.append(int(key))
        #         dicc[letra] += lista
        # print(dicc)
