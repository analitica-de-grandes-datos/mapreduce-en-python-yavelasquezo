#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:
        # elimino los espacios en blanco y divido por los 3 espacios que hay entre columnas
        dividir = row.strip().split("   ")
        columnaCero = dividir[0]
        columnaDos = dividir[2]
  
    
        sys.stdout.write(f"{columnaCero}\t{columnaDos}\n")
