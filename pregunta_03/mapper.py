#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys



if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #

    for row in sys.stdin:
        # limpio los espacios en blanco al final
        limpiarLinea = row.strip()
        
        #divido por por coma y obtengo las dos columnas que me interan       
        letra, numero = limpiarLinea.split(",") 

        # escribe al flujo estandar de salida
        sys.stdout.write(f"{letra}\t{numero}\n")
