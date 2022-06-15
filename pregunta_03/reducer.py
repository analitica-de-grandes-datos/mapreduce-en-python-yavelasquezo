#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import operator
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    dict = {}
    
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin: 
        key, valor = line.split("\t")
        valor = int(valor)
        dict[key] = valor
          
    sortedDict = sorted(dict.items(), key=operator.itemgetter(1))
    for linea in sortedDict:

        
        
        sys.stdout.write("{},{}\n".format(linea[0], linea[1]))
