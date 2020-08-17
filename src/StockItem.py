import uuid

class StockItem:
    def __init__(self, name):
        # todo: enter decription!
        """

        :param name:
        """
        # todo: argument check!
        self.name = name
        # todo: check if we need guid! I'm not definetly sure...
        self.guid = uuid.uuid4()

    def __str__(self):
        return self.name