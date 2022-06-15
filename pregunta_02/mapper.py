#
# >>> Escriba el codigo del mapper a partir de este punto <<<
# 
import sys

if __name__ == "__main__":
  for line in sys.stdin:

    lista=line.split(',')
    primeracol=lista[3]
    segundacol=lista[4]
    sys.stdout.write(f"{primeracol}\t{segundacol}\n")
