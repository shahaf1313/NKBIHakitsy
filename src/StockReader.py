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
    for index, barcode in north21stock['Barcode (Item)'].items():
        if barcode in north20stock['Barcode (Item)'].values:
            indicesToDrop.append(index)
    north2021stock = north21stock.drop(north21stock.index[indicesToDrop])
    north2021stock.to_excel(r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North '
                            r'Kiteboarding Unique 2021 Export By Barcode.xlsx')

def FindAnomalies():
    unique_barcode = pd.read_excel(
        r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North '
        r'Kiteboarding Unique 2021 Export By Barcode.xlsx', keep_default_na=False,
        converters={'Item': str, 'Barcode (Item)': str})
    unique_item = pd.read_excel(
        r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North '
        r'Kiteboarding Unique 2021 Export.xlsx', keep_default_na=False,
        converters={'Item': str, 'Barcode (Item)': str})

    indices_to_drop = []
    for index, barcode in unique_barcode['Barcode (Item)'].items():
        if barcode in unique_item['Barcode (Item)'].values:
            indices_to_drop.append(index)
    unique_barcode = unique_barcode.drop(unique_barcode.index[indices_to_drop])
    unique_barcode.to_excel(r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Add To Rivhit.xlsx')


def ReadStockFromExel(stock_file_path: str, year: str, header_row: int, default_columns_map: ColumnsMap = DefaultColumnsMap,
                      string_columns_names: list = DefaultStringColumns):
    stock = NorthStock()
    converters = {}
    for col_name in string_columns_names:
        converters[col_name] = str
    stock_file = pd.read_excel(stock_file_path, skiprows=header_row - 1, keep_default_na=False,
                               converters=converters)
    for index, row in stock_file.iterrows():
        prices = Prices(far_east_price=float('nan'), export_price=row[default_columns_map.export_price],
                        wholesale_price=float('nan'), retail_price=row[default_columns_map.retail_price],
                        currency=row[default_columns_map.currency])
        if default_columns_map.far_east_price in row.values:
            prices.farEastPrice = row[default_columns_map.far_east_price]
        stock.AddStockItem(name=row[default_columns_map.name],
                           year=year,
                           item_number=row[default_columns_map.serial_number],
                           barcode=row[default_columns_map.barcode],
                           size=row[default_columns_map.size],
                           color=row[default_columns_map.color],
                           prices=prices)
    return stock


FindAnomalies()