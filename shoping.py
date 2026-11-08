class shop:
    def __init__(self,buyar):
        self.buyar=buyar
        self.card=[]
    def  add_to_card (self,item):
        self.card.append(item)

riad = shop('riad')
riad.add_to_card('watch')
riad.add_to_card('moto')
print(riad.card)
ranu=shop('ranu')
ranu.add_to_card('hill')
ranu.add_to_card('churi')
print(ranu.card)