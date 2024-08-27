import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    print(line, end="")

    def separedString(a):
        lista = a.split(";")
        xlist = lista[0]
        ylist = lista[1]

        response = lcs(xlist, ylist)
        value = "".join(response)
        return value

    def lcs(xlist, ylist):
        if not xlist or not ylist:
            return []
        x, xs, y, ys = xlist[0], xlist[1:50], ylist[0], ylist[1:50]
        if x == y:
            return [x] + lcs(xs, ys)
        else:
            return max(lcs(xlist, ys), lcs(xs, ylist), key=len)

finalResult = separedString("XMJYAUZ;MZJAWXU")
print(finalResult)
MJAU
