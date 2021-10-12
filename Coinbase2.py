"""
Coinbase (https://www.coinbase.com/) is creating a new portfolio manager. 
They have hired you to create a prototype that manages a set of currencies in a portfolio. 
This system will include at least two different classes that you design. 
Minimum specifications:
    1.	Create some currency objects, which keep track of individual investments, their number of shares and their current price. 
    2.	Create some portfolio objects, which keeps track of a group of currency investments.  
        The portfolio should enable printing its current holdings, as well as the total value of their portfolio. 
        You should also include other things as you see fit.
    3.	Allow the user to sell currencies (reduce the shares), purchase currencies items (increase the shares), and 
    4.	Consider adding other functionality of your choosing (what else might they want to do?).
    5.	Create a menu so that the user can interact with the system 
        (e.g. to order an item press 1, to restock an item press 2...) Keep showing the menu until the user says stop (this will be done in a loop).
    6.	Print out the inventory of all items after all of the changes from the user, include how many of each one is currently available and print totals.
"""

class Portfolio:
# Attributes: CURRENCY Investments, Currency Holdings, Portfolio Total Value
    def __init__(self):
        self.holdings = []
        self.totalVal = 0

    def addHolding(self, newHolding):
        h = input("What are your holdings? ")
        self.holdings.append(h)
        self.holdings.append(newHolding)

    def printHoldings(self):
        print(self.holdings)

     

    


class Currency:
# Attributes: Investments, Number of Shares, Current Price
    def __init__(self, investments, shares, price):
        self.investments = investments
        self.shares = shares
        self.price = price

    def buy(self, sharesB):
        self.shares.append(sharesB)

    def sell(self, sharesS):
        self.shares.append(sharesS)

######################################################################

myPort = Portfolio()

