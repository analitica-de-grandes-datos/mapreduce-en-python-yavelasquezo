#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ =='__main__':

    curkey=None
    total=0
    maximo=0

    for line in sys.stdin:

        key,val=line.split('\t')
       
        val=int(val)

        if key == curkey:
            if val > maximo:

                maximo=val
                total=maximo
            else:
                val=maximo
                total=val

        else:
            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey,total))
                
            curkey=key
            maximo=val
            total=val
        
    sys.stdout.write("{}\t{}\n".format(curkey,total))
