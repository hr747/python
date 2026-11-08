class shopping:
    cat=[] 
    origin='china'
    def __init__(self,name,location):
        self.name='jamuna'
        self.location='dhaka'
    @staticmethod
    def multipay(a,b):
        print( a*b)
    @classmethod
    def purchase(self,item,price,amount):
        remaining=amount-price
        print(f'by:{item}for price:{price}and remaining:{remaining}')
shopping.purchase('lingi',400,1000)
shopping.multipay(5,6)


