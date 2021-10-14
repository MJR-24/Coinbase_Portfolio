"""
    Coinbase (https://www.coinbase.com/) is creating a new portfolio manager. 
    They have hired you to create a prototype that manages a set of currencies in a portfolio. 
    This system will include at least two different classes that you design. 
"""

class Portfolio:
    """ Portfolio class will:
            `Keep track of Currency Investments.
            `Print current Holdings.
            `Calculate and print Total Portfolio Value.
    """
    def __init__(self):
        self.holdings = []
        self.holdingsCost = []
        self.shares = []
        self.sharesTotal = 0
        self.totalVal = 0

    def addHolding(self):
        # Adds Holdings in a loop until the user says stop.
        h = input("What is the name of one of your holdings? ")
        self.holdings.append(h)

        p = input("What is the price of that holding? ")
        self.totalVal = self.totalVal + float(p)
        self.holdingsCost.append(float(p))

        s = input("How many shares do you hold? ")
        self.sharesTotal = self.sharesTotal + int(s)
        self.shares.append(int(s))

        ans = input("Add another holding (y/n)? ")
        if ans == "y" or ans == "Y":
            repeat = True
        if ans == 'n' or ans == "N":
            repeat = False

        while repeat == True:
            h = input("What is the name of one of your holdings? ")
            self.holdings.append(h)

            p = input("What is the price of that holding? ")
            self.totalVal = self.totalVal + float(p)
            self.holdingsCost.append(float(p))

            s = input("How many shares do you hold? ")
            self.sharesTotal = self.sharesTotal + int(s)
            self.shares.append(int(s))

            ans = input("Add another holding (y/n)? ")
            if ans == "y" or ans == "Y":
                repeat = True
            elif ans == 'n' or ans == "N":
                repeat = False

        #zipLists = print(dict(zip(self.holdings, self.holdingsCost)))
        #return zipLists

    def findTotal(self):
        prntTotal = print(f"Total Portfolio Value: {self.totalVal:.2f}")
        return prntTotal
    
    def printHoldings(self):
        print("Current Holdings: ")
        for i in range(len(self.holdings)):
            print(f"-{self.holdings[i]}")

class Currency(Portfolio):
    """ Currency class will:
            Keep track of Individual Investments
            Keep track of Number of Shares
            Keep track of Current Price of Shares
            Allow user to Sell currencies (Reduce Shares)
            Allow user to Buy currencies (Increase Shares)
    """
    def __init__(self, investment, price):
        self.investment = investment
        
        self.price = price

    def buy(self):
        super().__init__()
        print(self.sharesTotal)

    def sell(self, sharesS):
        self.shares.append(sharesS)

######################################################################
# TODO: Create a menu for user to interact with system.
        # Keep showing menu until user says to stop.

# TODO: Print inventory of all items after all changes from user. 
        # Including: How many of each one is currently available &
                    # Print the totals. 
######################################################################

myPort = Portfolio()
myCurr = Currency()

myPort.addHolding()
myPort.printHoldings()
myPort.findTotal()

myCurr.buy()

