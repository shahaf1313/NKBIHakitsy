class Ammounts:
    def __init__(self, itemsInStock, itemsSold, itemsBought):
        # todo: enter decription!
        """
        Enter description......
        :param itemsInStock: int nub
        :param itemsSold:
        :param itemsBought:
        """
        # todo: argument check!
        self.itemsInStock = itemsInStock
        self.itemsSold = itemsSold
        self.itemsBought = itemsBought


class Prices:
    def __init__(self, farEastPrice, exportPrice, wholesalePrice, retailPrice, currency):
        # todo: enter decription!
        """
        Enter description......
        :param farEastPrice:
        :param exportPrice:
        :param wholesalePrice:
        :param retailPrice:
        :param currency:
        """
        # todo: argument check!
        self.farEastPrice = farEastPrice
        self.exportPrice = exportPrice
        self.wholesalePrice = wholesalePrice
        self.retailPrice = retailPrice
        self.currency = currency


class StockState:
    def __init__(self,
                 prices: type(Prices) = Prices(0, 0, 0, 0, "dollar"),
                 ammounts: type(Ammounts) = Ammounts(0, 0, 0)):
        # todo: enter decription!
        """
        This function initializes StockState with zeros for Ammounts and Prices
        """
        # todo: argument check!
        self.prices = prices
        self.ammounts = ammounts
