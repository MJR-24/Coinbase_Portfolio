class Currency:
    def __init__(self, nameC, priceC) -> None:
        self.nc = nameC
        self.np = priceC
        self.sharesC = 0

    def __str__(self) -> str:
        return f'{self.nc}: {self.np} share(s)'

    def addShares(self, numShares):
        self.sharesC += int(numShares)

    def subtractShares(self, numShares):
        self.sharesC -= int(numShares)

class Portfolio(Currency):
    def __init__(self, namePort) -> None:
        self.namePort = namePort
        self.holdings = []
        self.holdingShares = []
        self.holdingPrices = []

    def addCurrency(self, newCurr, newShares, newPrices):
        self.holdings.append(newCurr)
        self.holdingShares.append(newShares)
        self.holdingPrices.append(newPrices)

    def inventory(self):
        print(f'{self.namePort} Summary:')
        print(f'You currently own {len(self.holdings)} holding(s).')
        for h, s in zip(self.holdings, self.holdingShares):
            print(f'{h}: {s} share(s)')    

    def totalInventory(self):
        total = 0
        for n, p in zip(self.holdingShares, self.holdingPrices):
            total += int(n) * float(p)
        print(f"Total value of holdings: {total}")

    def addCurrShares(self):
        print('Which currency would you like to work with: ')
        for idx, curr in enumerate(self.holdings):
            print(f'{idx}: {str(curr)}')
        choice = int(input('-- '))
        num = int(input(f'How many shares of {self.holdings[choice]} would you like to buy? '))
        self.holdingShares[choice] += num
        
    def subtractShares(self):
        print('Which currency would you like to work with: ')
        for idx, curr in enumerate(self.holdings):
            print(f'{idx}: {str(curr)}')
        choice = int(input('-- '))
        num = int(input(f'How many shares of {self.holdings[choice]} would you like to sell? '))
        self.holdingShares[choice] -= num

##########

portName = str(input('Name your portfolio: '))
p = Portfolio(portName)
numCurr = int(input('How many currencies do you hold? '))

for n in range(numCurr):
    nameCurr = str(input('Currency name: '))
    priceCurr = float(input(f'{nameCurr} price: '))
    sharesCurr = int(input(f'Number of {nameCurr} shares: '))
    p.addCurrency(nameCurr, sharesCurr, priceCurr)
    c = Currency(nameCurr, priceCurr)

while True:
    print("\n\t\t************Crypto Currency Portfolio**************\n")
    print("\nPlease choose an action to perform: ")
    ans = input("""\t\t  A: Print Inventory     B: Buy Shares
                  C: Sell Shares         E. Exit 
            
                    Please enter your choice: """)
    if (ans == 'A' or ans == 'a'):
        p.inventory()
        p.totalInventory()
    elif (ans == 'B' or ans == 'b'):
        p.addCurrShares()
    elif (ans == 'C' or ans == 'c'):
        p.subtractShares()
    elif (ans == 'E' or ans == 'e'):
        break
    