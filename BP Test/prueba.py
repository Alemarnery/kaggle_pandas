def lcs_recursive(xlist, ylist):
    if not xlist or not ylist:
        return []
    x, xs, y, ys, = xlist[0], xlist[1:50], ylist[0], ylist[1:50]
    print(xs)
    if x == y:
        return [x] + lcs_recursive(xs, ys)
    else:
        return max(lcs_recursive(xlist, ys), lcs_recursive(xs, ylist), key=len)


s1 = 'XMJYAUZ'
s2 = 'MZJAWXU'

print(lcs_recursive(s1, s2))
