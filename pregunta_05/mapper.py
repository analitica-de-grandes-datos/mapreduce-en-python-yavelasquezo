#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:
        # elimino los espacios en blanco y divido por los 3 espacios que hay entre columnas
        dividir = row.strip().split("   ")
        columnaUno = dividir[1]
        fechaDividida = columnaUno.split("-")
        mes = fechaDividida[1]
  
    
        sys.stdout.write(f"{mes}\t1\n")
