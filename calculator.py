class  calculator:
    def add(self, n1,n2):
        sum=n1+n2
        return sum
    def dadd (self, n1,n2):
        sum2= abs(n1-n2)
        return sum2
    def multi(self,n1,n2):
        sum3=n1*n2
        return sum3
    def mxx(self,n1,n2):
        sum4=n1/n2
        return sum4
c=calculator()
print(c.add(2,3))
print(c.dadd(4,5))
print(c.multi(6,7))
print(c.mxx(8,2))

    
        