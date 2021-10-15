from PortfolioClass import Portfolio
from CurrencyClass import Currency
import sys

def main():
        menu()

def menu():
        print("\t\t************Crypto Currency Portfolio**************\n")

        choice = input("""\t\t\t  A: Add Holdings     B: Buy Shares
                          C: Sell Shares      D: Print Inventory
                                        E. Exit 
                    
                      Please enter your choice: """)

        if choice == "A" or choice =="a":
            numCurrencies = int(input('How many currencies do you hold? '))
            currencies = {}

            for n in range(numCurrencies):
                if n == 0:
                    newCurrency = input('Please enter currency name: ')
                    newCurrPrice = input('What is the stock price of that currency? ')
                    newCurrAmt = input('How many shares do you own of that currency? ')
                else:
                    newCurrency = input('Please enter another currency name: ')
                    newCurrPrice = input('What is the stock price of that currency? ')
                    newCurrAmt = input('How many shares do you own of that currency? ')
                currencies[newCurrency, newCurrPrice, newCurrAmt] = Currency(newCurrency, newCurrPrice, newCurrAmt)

            for currency,price,amount in currencies:
                print(Currency(currency,price,amount))
                
        elif choice == "B" or choice =="b":
            pass
        elif choice == "C" or choice =="c":
            pass
        elif choice == "D" or choice =="d":
            pass
        elif choice=="E" or choice=="e":
            sys.exit
        else:
            print("You must only select either A or B")
            print("Please try again")
            menu()



menu()



