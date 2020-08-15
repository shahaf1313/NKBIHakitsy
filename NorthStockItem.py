class NorthStockItem:
    def __init__(self, name, guid):
        self._name = name
        self._guid = guid

    def __str__(self):
        return self._name