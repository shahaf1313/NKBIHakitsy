from StockState import *
class StockItem:
    def __init__(self, name, guid):
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
        self._name = name
        self._guid = guid
        self._subItemDetails = {}

    def __str__(self):
        return self._name