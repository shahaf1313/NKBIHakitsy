import uuid


class StockItem:
    def __init__(self, name):
        """
        This function initializes the class.
        :param name: Name (str) of the StockItem.
        """
        self.name = name
        # todo: check if we need guid! I'm not definetly sure...
        self.guid = uuid.uuid4()

    def __str__(self):
        return self.name
