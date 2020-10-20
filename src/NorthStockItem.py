from src.StockItem import *


class Amounts:
    def __init__(self,
                 items_imported: int = 0,
                 items_in_stock: int = 0,
                 items_sold=None):
        """
        This function Initializes the Amounts class.
        :param items_imported: Number of items imported from a specific item type.
        :param items_in_stock: Number of items in stock from a specific item type.
        :param items_sold: Dictionary with <key, value> of <date, int> indicating how many items were sold in which
        dates. If the key is null - the date is unknown.
        """
        if items_sold is None:
            items_sold = {}
        self.items_in_stock = items_in_stock
        self.items_sold = items_sold
        self.items_imported = items_imported


class Prices:
    def __init__(self,
                 far_east_price: float = 0,
                 export_price: float = 0,
                 wholesale_price: float = 0,
                 retail_price: float = 0,
                 currency: str = ""):
        """
        This function initializes class Prices.
        :param far_east_price: Float. Self explained.
        :param export_price: Float. Self explained.
        :param wholesale_price: Float. Self explained.
        :param retail_price: Float. Self explained.
        :param currency: String that indicates what is the currency of all of the prices above.
        """
        self.far_east_price = far_east_price
        self.export_price = export_price
        self.wholesale_price = wholesale_price
        self.retail_price = retail_price
        self.currency = currency

class NorthStockItem(StockItem):
    def __init__(self, name, year, item_number, barcode, size, color, prices = None, amounts = None):
        """
        This function initializes the class.
        :param name: name of the current NorthStockItem.
        """
        super().__init__(name, year, item_number, barcode)
        self.size = size
        self.color = color
        self.prices = prices if prices is not None else Prices()
        self.amounts = amounts if amounts is not None else Amounts()