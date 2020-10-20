from src.StockItem import *
from src.StockState import *
import time


class NorthStockItem(StockItem):
    def __init__(self, name, year, item_number, barcode):
        """
        This function initializes the class.
        :param name: name of the current NorthStockItem.
        """
        super().__init__(name, year, item_number, barcode)
        self.size_color_dict = {}

    def updateStockItemPrices(self, size: str, color: str, prices: Prices):
        """
        This function adds key (size, color) to the subItemsDetails dictionary, and initializes Prices to be the given
        prices parameter. If this tuple already exists - the function finds it and updates Prices accordingly.
        :param size: Size string of the current item.
        :param color: Color string of the current item.
        :param prices: New/updated prices of the given stock item.
        """
        if (size, color) in self.size_color_dict:
            self.size_color_dict[(size, color)].prices = prices
        else:
            self.size_color_dict[(size, color)] = StockState(prices=prices)

    def updateStockItemAmounts(self, size: str, color: str, amounts: Amounts):
        """
        This function adds key (size, color) to the subItemsDetails dictionary, and initializes Amounts to be the given
        prices parameter. If this tuple already exists - the function finds it and updates Prices accordingly.
        :param size: Size string of the current item.
        :param color: Color string of the current item.
        :param amounts: New/updated prices of the given stock item.
        """
        if (size, color) in self.size_color_dict:
            self.size_color_dict[(size, color)].amounts = amounts
        else:
            self.size_color_dict[(size, color)] = StockState(amounts=amounts)

