from src.NorthStockItem import *
from src.StockState import *


class NorthStock:
    """
    This function initializes an empty stock.
    """

    def __init__(self):
        self.stock = {}

    def addStockItem(self,
                     name: str,
                     year: str,
                     serial_number: str,
                     barcode: str,
                     size: str = None,
                     color: str = None,
                     prices: Prices = None,
                     amounts: Amounts = None):

        if serial_number not in self.stock.keys():
            current_north_stock_item = NorthStockItem(name, year, serial_number, barcode)
            self.stock[serial_number] = current_north_stock_item
        else:
            current_north_stock_item = self.stock[serial_number]

        if (size is not None) and (color is not None):
            if (size, color) not in current_north_stock_item.size_color_dict:
                current_stock_state = StockState()
                current_north_stock_item.size_color_dict[(size, color)] = current_stock_state
            else:
                current_stock_state = current_north_stock_item.size_color_dict[(size, color)]

            if prices is not None:
                current_stock_state.prices = prices

            if amounts is not None:
                current_stock_state.amounts = amounts

    # def setStockItemsDetails(self,
    #                          name: str,
    #                          size: str,
    #                          color: str,
    #                          prices: Prices = None,
    #                          amounts: Amounts = None):
    #     """
    #     todo: document!
    #     :param name:
    #     :param size:
    #     :param color:
    #     :param prices:
    #     :param amounts:
    #     :return:
    #     """
    #     for item in self.stock:
    #         if name == item.name:
    #             if prices is not None:
    #                 item.updateStockItemPrices(size, color, prices)
    #             if amounts is not None:
    #                 item.updateStockItemAmounts(size, color, amounts)
    #             break
