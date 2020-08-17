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
        self._itemsInStock = itemsInStock
        self._itemsSold = itemsSold
        self._itemsBought = itemsBought


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
        self._farEastPrice = farEastPrice
        self._exportPrice = exportPrice
        self._wholesalePrice = wholesalePrice
        self._retailPrice = retailPrice
        self._currency = currency


class StockState:
    def __init__(self):
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
        self._ammounts = Ammounts(0, 0, 0)
        self._prices = Prices(0, 0, 0, 0, 0)
