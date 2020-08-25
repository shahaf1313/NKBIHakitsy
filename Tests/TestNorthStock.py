import unittest
import datetime
from src.NorthStock import *


class TestNorthStockClass(unittest.TestCase):
    def test_north_stock(self):
        north = NorthStock()
        north.addStockItem("Orbit")
        north.addStockItem("Pulse")
        orbit10Price = Prices(10, 15, 25, 50, "dollar")
        pulse10Price = Prices(13, 18, 28, 53, "dollar")
        orbit10Amounts = Amounts(10, 9, {datetime.date: 1})
        pulse10Amounts = Amounts(20, 19, {datetime.date: 1})
        north.setStockItemsDetails("Orbit", "10", "red", orbit10Price, orbit10Amounts)
        north.setStockItemsDetails("Orbit", "10", "green", orbit10Price, orbit10Amounts)
        north.setStockItemsDetails("Pulse", "10", "red", pulse10Price, pulse10Amounts)
        north.setStockItemsDetails("Pulse", "10", "green", pulse10Price, pulse10Amounts)
        self.assertEqual(len(north.stock), 2)
        self.assertEqual(len(north.stock[0].subItemDetails), 2)
        self.assertEqual(len(north.stock[1].subItemDetails), 2)

if __name__ == '__main__':
    unittest.main()

