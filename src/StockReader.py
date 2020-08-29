import pandas as pd
from src.NorthStock import *
from src.Constants import *


def ExportUniqueStock2021():
    north20stock = pd.read_excel(
        r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North '
        r'Kiteboarding 2020 Export Updated Prices.xlsx', skiprows=9, keep_default_na=False,
        converters={'Item': str, 'Barcode (Item)': str})
    north21stock = pd.read_excel(
        r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North '
        r'Kiteboarding 2021 Export.xlsx', skiprows=10, keep_default_na=False,
        converters={'Item': str, 'Barcode (Item)': str})

    indicesToDrop = []
    for index, barcode in north21stock['Item'].items():
        if barcode in north20stock['Item'].values:
            indicesToDrop.append(index)
    north2021stock = north21stock.drop(north21stock.index[indicesToDrop])
    north2021stock.to_excel(r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North '
                            r'Kiteboarding Unique 2021 Export.xlsx')


def ReadStockFromExel(stock_file_path: str, year: str, header_row: int, default_columns_map: ColumnsMap = DefaultColumnsMap,
                      string_columns_names: list = DefaultStringColumns):
    stock = NorthStock()
    converters = {}
    for col_name in string_columns_names:
        converters[col_name] = str
    stock_file = pd.read_excel(stock_file_path, skiprows=header_row - 1, keep_default_na=False,
                               converters=converters)
    for index, row in stock_file.iterrows():
        prices = Prices(farEastPrice=float('nan'), exportPrice=row[default_columns_map.export_price],
                        wholesalePrice=float('nan'), retailPrice=row[default_columns_map.retail_price],
                        currency=row[default_columns_map.currency])
        if default_columns_map.far_east_price in row.values:
            prices.farEastPrice = row[default_columns_map.far_east_price]
        stock.addStockItem(name=row[default_columns_map.name],
                           year=year,
                           serial_number=row[default_columns_map.serial_number],
                           barcode=row[default_columns_map.barcode],
                           size=row[default_columns_map.size],
                           color=row[default_columns_map.color],
                           prices=prices)
    return stock


stock2020path = r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North Kiteboarding 2020 Export Updated Prices.xlsx'
header_row_2020 = 10
stock2020 = ReadStockFromExel(stock2020path, 'MY20', header_row_2020)
k = 1