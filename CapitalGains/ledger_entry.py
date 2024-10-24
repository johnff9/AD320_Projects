from linked_deque import LinkedDeque


class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.purchases = LinkedDeque()  # Using LinkedDeque for managing stock purchases

    def add_purchase(self, new_purchase):
        self.purchases.add_to_back(new_purchase)  # Add a new purchase to the back of the deque

    def remove_purchase(self, shares_to_sell):
        total_sold = 0
        while total_sold < shares_to_sell and not self.purchases.is_empty():
            first_purchase = self.purchases.get_front()  # Access first item (FIFO)
            if first_purchase.shares <= shares_to_sell - total_sold:
                total_sold += first_purchase.shares
                self.purchases.remove_front()  # Remove from front once fully sold
            else:
                first_purchase.shares -= (shares_to_sell - total_sold)
                total_sold = shares_to_sell
        return total_sold

    def display_entry(self):
        current = self.purchases.front
        result = []
        while current:
            purchase = current.get_data()
            result.append(f"{purchase.cost_per_share} ({purchase.shares} shares)")
            current = current.get_next_node()
        return f"{self.stock_symbol}: " + ", ".join(result)
