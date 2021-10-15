from PortfolioClass import Portfolio

class Currency:
    def __init__(self, name, price, amount):
        self.name = str(name)
        self.price = float(price)
        self.amount = int(amount)

    def __str__(self) -> str:
        return f'{self.name}: {self.amount} share(s)'

    #def setCurrency(self):
        

