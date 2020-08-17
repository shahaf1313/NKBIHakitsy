from src.StockItem import *
from src.StockState import *


class NorthStockItem(StockItem):
    def __init__(self, name):
        """
        This function initializes the class.
        :param name: name of the current NorthStockItem.
        """
        super().__init__(name)
        self.subItemDetails = {}

    def addStockItemPrices(self, size: str, color: str, prices: Prices):
        """
        This function adds key (size, color) to the subItemsDetails dictionary, and initializes Prices to be the given
        prices parameter. If this tuple already exists - the function finds it and updates Prices accordingly.
        :param size: Size string of the current item.
        :param color: Color string of the current item.
        :param prices: New/updated prices of the given stock item.
        """
        if (size, color) in self.subItemDetails:
            self.subItemDetails[(size, color)].prices = prices
        else:
            self.subItemDetails[(size, color)] = StockState(prices=prices)

