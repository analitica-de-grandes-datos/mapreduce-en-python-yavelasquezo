#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ =='__main__':

    curkey=None
    maximo=[]

    for line in sys.stdin:

        key,val=line.split('\t')
        val=int(val)

        if key == curkey:

            maximo.append(val)

        else:
            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey,total))
            
            curkey=key
            maximo.append[val]
        total=max(maximo)
        maximo=0
    sys.stdout.write("{}\t{}\n".format(curkey,total))
