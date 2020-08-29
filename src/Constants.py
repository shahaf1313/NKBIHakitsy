class ColumnsMap:
    def __init__(self,
                 name='Item Description',
                 serial_number='Item',
                 color='Color Description',
                 size='Size',
                 barcode='Barcode (Item)',
                 currency='Currency',
                 retail_price='Suggested Retail Price',
                 export_price='Export Price',
                 far_east_price='3PL China Price'
                 ):
        self.name = name
        self.serial_number = serial_number
        self.color = color
        self.size = size
        self.barcode = barcode
        self.currency = currency
        self.retail_price = retail_price
        self.export_price = export_price
        self.far_east_price = far_east_price


DefaultColumnsMap = ColumnsMap()
DefaultStringColumns = ['Item Description', 'Color Description', 'Size', 'Barcode (Item)', 'Currency', 'Item']
NorthEuroShekelRate = 4.1
NorthDollarShekelRate = 3.6
