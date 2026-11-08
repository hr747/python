class shoping:
    def __init__(self, name):
        self.name = name
        self.card = []

    def add_t0_card(self, item, price, quntity):
        prodacet = {'item': item, 'price': price, 'quntity': quntity}
        self.card.append(prodacet)

    def remove_most_expensive(self):
        if not self.card:

            return

        most_expensive = max(
            self.card, key=lambda x: x['price'] * x['quntity'])

        self.card.remove(most_expensive)

    def cackout(self, amount):
        total = 0
        for item in self.card:
            total += item['price']*item['quntity']
        print(f"your total pay ammount : {total}")
        if amount < total:
            print(f'pay mor money {total-amount}')
            self.remove_most_expensive()
        elif amount > total:
            print(f'you back {total-amount}')
        else:
            print(f'payment ok')


riad = shoping('all momin')
riad.add_t0_card('alui', 20, 5)
riad.add_t0_card('lobon', 5, 2)
riad.add_t0_card('cini', 10, 6)
riad.add_t0_card('rosun', 6, 8)
riad.cackout(28)

