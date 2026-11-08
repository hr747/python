class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdrow = 300
        self.max_withdrow = 100000

    def get_balance(self):
        return self.balance

    def dp(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'your amount is {self.get_balance()}')
        else:
            print(f'not prosible')

    def wd(self, amount):
        if amount < self.min_withdrow:
            print(
                f'Not possible! Minimum withdrawal amount is {self.min_withdrow}')
        elif amount > self.max_withdrow:
            print(
                f'Not possible! Maximum withdrawal amount is {self.max_withdrow}')
        elif amount > self.balance:
            print('Not possible! Insufficient balance.')
        else:
            self.balance -= amount

            print(f'Successful. Your balance is: {self.get_balance()}')


dppl = bank(20000)
dppl.wd(100)
dppl.wd(1000000)
dppl.wd(1000)
dppl.dp(5000)
