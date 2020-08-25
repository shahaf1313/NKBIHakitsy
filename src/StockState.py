class Amounts:
    def __init__(self, itemsImported: int, itemsInStock: int,  itemsSold: dict):
        """
        This function Initializes the Amounts class.
        :param itemsImported: Number of items imported from a specific item type.
        :param itemsInStock: Number of items in stock from a specific item type.
        :param itemsSold: Dictionary with <key, value> of <date, int> indicating how many items were sold in which
        dates. If the key is null - the date is unknown.
        """
        self.itemsInStock = itemsInStock
        self.itemsSold = itemsSold
        self.sellingDate = []
        self.itemsImported = itemsImported


class Prices:
    def __init__(self,
                 farEastPrice: float,
                 exportPrice: float,
                 wholesalePrice: float,
                 retailPrice: float,
                 currency: str):
        """
        This function initializes class Prices.
        :param farEastPrice: Float. Self explained.
        :param exportPrice: Float. Self explained.
        :param wholesalePrice: Float. Self explained.
        :param retailPrice: Float. Self explained.
        :param currency: String that indicates what is the currency of all of the prices above.
        """
        self.farEastPrice = farEastPrice
        self.exportPrice = exportPrice
        self.wholesalePrice = wholesalePrice
        self.retailPrice = retailPrice
        self.currency = currency


class StockState:
    def __init__(self,
                 prices: Prices = Prices(0, 0, 0, 0, "dollar"),
                 amounts: Amounts = Amounts(0, 0, {})):
        """
        This function initializes StockState class. If given - initial values are transferred to Amounts and Prices.
        If not given, Amounts and Prices are automatically created, initialized to zero.
        :param prices:
        :param amounts:
        """
        self.prices = prices
        self.amounts = amounts
