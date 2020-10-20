from src.NorthStockItem import *
import pandas as pd
from src.Constants import *


class NorthStockException(Exception):
    def __init__(self, message):
        super.__init__()
        self.message = message

class NorthStock:
    """
    This function initializes an empty stock.
    """

    def __init__(self):
        self.stock = {}

    def AddStockItem(self,
                     name: str,
                     year: str,
                     item_number: str,
                     barcode: str,
                     size: str = None,
                     color: str = None,
                     prices: Prices = None,
                     amounts: Amounts = None):

        if barcode not in self.stock.keys():
            self.stock[barcode] = NorthStockItem(name, year, item_number, barcode, size, color, prices, amounts)
        else:
            raise NorthStockException("Tried to add an item that already in stock!")

    def ReadStockFromExel(self, stock_file_path: str, year: str, header_row: int,
                          default_columns_map: ColumnsMap = DefaultColumnsMap,
                          string_columns_names: list = DefaultStringColumns):
        converters = {}
        for col_name in string_columns_names:
            converters[col_name] = str
        stock_file = pd.read_excel(stock_file_path, skiprows=header_row - 1, keep_default_na=False,
                                   converters=converters)
        for index, row in stock_file.iterrows():
            if row[default_columns_map.barcode] in self.stock.keys():
                print("ReadStockFromExel :: item %s %s %s is already in stock!" % (row[default_columns_map.name], row[default_columns_map.size], row[default_columns_map.color]))
                continue
            prices = Prices(far_east_price=float('nan'), export_price=row[default_columns_map.export_price],
                            wholesale_price=float('nan'), retail_price=row[default_columns_map.retail_price],
                            currency=row[default_columns_map.currency])
            if default_columns_map.far_east_price in row.values:
                prices.farEastPrice = row[default_columns_map.far_east_price]
            self.AddStockItem(name=row[default_columns_map.name],
                              year=year,
                              item_number=row[default_columns_map.serial_number],
                              barcode=row[default_columns_map.barcode],
                              size=row[default_columns_map.size],
                              color=row[default_columns_map.color],
                              prices=prices)

