class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=str(n)
        sums=0
        prod=1
        for i in num:
            sums=sums+int(i)
            prod=prod*int(i)
        if n % (sums+prod) ==0:
            return True
        else: 
            return False
        