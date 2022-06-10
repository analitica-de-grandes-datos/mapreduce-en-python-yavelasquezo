#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

file=open("credit.csv", "r").readlines()

file=[z.replace("\n","")for z in file]
file=[z.split(",") for z in file]
lista=[]

#Map
for i in file:
  lista.append(i[2])
lista.sort(reverse=False)
result=lista
