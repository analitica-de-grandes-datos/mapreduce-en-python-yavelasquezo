#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

from functools import reduce
def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc


result=str(reduce(
    make_counts,
    lista,
    {},
))
