#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import operator
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    lista = []
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
   

    for line in sys.stdin:

        key, fecha, valor = line.split("\t")
        valor = int(valor)
        tupla = key, fecha, valor
        lista.append(tupla)
          
    sortedDict = sorted(lista, key=operator.itemgetter(2))
    del sortedDict[6:]

    for linea in sortedDict:

        sys.stdout.write("{}   {}   {}\n".format(linea[0], linea[1], linea[2]))
