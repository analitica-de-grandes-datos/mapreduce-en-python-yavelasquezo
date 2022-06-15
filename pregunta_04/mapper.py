#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
   
    #for line in sys.stdin:
    for row in sys.stdin:
        # elimino los espacios en blanco y divido por los 3 espacios que hay entre columnas
        dividir = row.strip().split("   ")
        columnaUno = dividir[0]
    
        sys.stdout.write(f"{columnaUno}\t1\n")
