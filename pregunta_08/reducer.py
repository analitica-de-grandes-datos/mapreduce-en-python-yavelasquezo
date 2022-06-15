#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from collections import defaultdict
import operator
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    miDict = defaultdict(list)
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)
        miDict[key].append(val)

    for clave, lista in miDict.items():
        suma = round(sum(lista), 1)
        promedio = sum(lista)/len(lista)

        valores = [clave, suma, promedio]  
           
        sys.stdout.write("{}\t{}\t{}\n".format(valores[0], valores[1], valores[2]))
