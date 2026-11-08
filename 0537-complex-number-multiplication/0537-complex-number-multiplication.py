class Solution:
    def complexNumberMultiply(self, a, b):
        ind1 = a.index("+")
        ind2 = b.index("+")
        x1, y1 = int(a[:ind1]), int(a[ind1+1:-1])
        x2, y2 = int(b[:ind2]), int(b[ind2+1:-1])
        return str(x1*x2-y1*y2) + "+" + str(x1*y2+x2*y1)+"i"