"""
    Coinbase (https://www.coinbase.com/) is creating a new portfolio manager. 
    They have hired you to create a prototype that manages a set of currencies in a portfolio. 
    This system will include at least two different classes that you design. 
"""

class Portfolio:
    """ Portfolio class will:
            Keep track of Currency Investments.
            Print current Holdings.
            Calculate and print Total Portfolio Value.
    """
    def __init__(self):
        self.holdings = []
        self.holdingsCost = []
        self.totalVal = 0

    def addHolding(self):
        # Adds Holdings in a loop until the user says stop.
        h = input("What are your holdings? ")
        self.holdings.append(h)

        p = input("What is the price of that holding? ")
        self.totalVal = self.totalVal + int(p)
        self.holdingsCost.append(f'${p}')

        ans = input("Add another holding? ")

        while ans == 'yes' or ans == 'Yes':
            if ans == 'yes' or ans == 'Yes':
                h = input("What are your holdings? ")
                self.holdings.append(h)
                p = input("What is the price of that holding? ")
                self.totalVal = self.totalVal + int(p)
                self.holdingsCost.append(f'${p}')
                ans = input("Add another holding? ")
            else:
                pass

    def findTotal(self):
        pass

class Currency:
    """ Currency class will:
            Keep track of Individual Investments
            Keep track of Number of Shares
            Keep track of Current Price of Shares
            Allow user to Sell currencies (Reduce Shares)
            Allow user to Buy currencies (Increase Shares)
    """
    def __init__(self, investments, shares, price):
        self.investments = investments
        self.shares = shares
        self.price = price

    def buy(self, sharesB):
        self.shares.append(sharesB)

    def sell(self, sharesS):
        self.shares.append(sharesS)

# TODO: Create a menu for user to interact with system.
        # Keep showing menu until user says to stop.

# TODO: Print inventory of all items after all changes from user. 
        # Including: How many of each one is currently available &
                    # Print the totals. 
######################################################################

myPort = Portfolio()
myPort.addHolding()

print(myPort.holdings)
print(myPort.holdingsCost)