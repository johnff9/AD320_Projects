from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase


class StockLedger:
    def __init__(self):
        self.ledger = {}

    def buy(self, stock_symbol, shares_bought, price_per_share):
        if stock_symbol not in self.ledger:
            self.ledger[stock_symbol] = LedgerEntry(stock_symbol)
        new_purchase = StockPurchase(price_per_share, shares_bought)
        self.ledger[stock_symbol].add_purchase(new_purchase)

    def sell(self, stock_symbol, shares_sold, price_per_share):
        if stock_symbol in self.ledger:
            sold_shares = self.ledger[stock_symbol].remove_purchase(shares_sold)
            if sold_shares < shares_sold:
                print(f"Warning: Only {sold_shares} shares sold from {stock_symbol}, not enough shares available.")
        else:
            print(f"No {stock_symbol} in ledger to sell.")

    def display_ledger(self):
        print("---- Stock Ledger ----")
        for entry in self.ledger.values():
            print(entry.display_entry())

    def contains(self, stock_symbol):
        return stock_symbol in self.ledger

    def get_entry(self, stock_symbol):
        return self.ledger.get(stock_symbol, None)
