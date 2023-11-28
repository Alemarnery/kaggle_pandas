

def split_string(string):

    if not string:
        return []
    lista = string.split(";")

    xlist = lista[0]
    ylist = lista[1]

    def lcs(alist, blist):
        a, al, b, bl = alist[0], alist[1:50], blist[0], blist[1:50]
        if a == b:
            return [a] + lcs(al, bl)
        else:
            return max(lcs(alist, bl), lcs(al, blist))

    lcs(xlist, ylist)


print(split_string("XMJYAUZ;MZJAWXU"))
