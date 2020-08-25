from src.NorthStockItem import *
import string


class NorthStock:
    """
    This function initializes an empty stock.
    """
    def __init__(self):
        self.stock = []

    def addStockItem(self, name: str):
        for item in self.stock:
            if item.name == name:
                return
        self.stock.append(NorthStockItem(name))

    def setStockItemsDetails(self,
                             name: str,
                             size: str,
                             color: str,
                             prices: Prices = None,
                             amounts: Amounts = None):
        """
        todo: document!
        :param name:
        :param size:
        :param color:
        :param prices:
        :param amounts:
        :return:
        """
        for item in self.stock:
            if name == item.name:
                if prices is not None:
                    item.updateStockItemPrices(size, color, prices)
                if amounts is not None:
                    item.updateStockItemAmounts(size, color, amounts)
                break


