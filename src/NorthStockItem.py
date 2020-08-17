from src.StockItem import *
from src.StockState import *


class NorthStockItem(StockItem):
    def __init__(self, name):
        super().__init__(name)
        self.subItemDetails = {}

    def addStockItemPrices(self, size: str, color: str, prices: type(Prices)):
        if not ((size, color) in self.subItemDetails):
            self.subItemDetails[(size, color)] = StockState(prices=prices)
        else:
            self.subItemDetails[(size, color)].prices = prices
