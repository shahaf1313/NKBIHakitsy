class StockItem:
    def __init__(self, name: str, year: str, serial_number: str, barcode: str):
        """
        This function initializes the class.
        :param name: Name (str) of the StockItem.
        :param year: Year (str) of the StockItem.
        :param serial_number (str) Serial number of the StockItem.
        :param barcode Barcode (str) of the StockItem.
        """
        self.name = name
        self.year = year
        self.serial_number = serial_number
        self.barcode = barcode

    def __str__(self):
        return "Name - %s %s, Serial Number - %s" % (self.name, self.year, self.serial_number)
