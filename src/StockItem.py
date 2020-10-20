class StockItem:
    def __init__(self, name: str, year: str, item_number: str, barcode: str):
        """
        This function initializes the class.
        :param name: Name (str) of the StockItem.
        :param year: Year (str) of the StockItem.
        :param item_number (str) Serial number of the StockItem.
        :param barcode Barcode (str) of the StockItem.
        """
        self.name = name
        self.year = year
        self.item_number = item_number
        self.barcode = barcode

    def __str__(self):
        return "Name - %s %s, Serial Number - %s, Barcode - %s" % (self.name, self.year, self.item_number, self.barcode)
