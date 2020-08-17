import unittest
from src.NorthStockItem import *
from src.StockState import *


class TestNorthStock(unittest.TestCase):
    def test_AddStockItemPrices(self):
        northItem = NorthStockItem("Orbit")
        self.assertIsNotNone(northItem)
        p = Prices(10, 15, 25, 50, "dollar")
        northItem.addStockItemPrices("10", "green", p)
        self.assertIs(isinstance(northItem.subItemDetails[("10", "green")].prices, Prices), True)
        self.assertEqual(northItem.subItemDetails[("10", "green")].prices.farEastPrice, 10)
        self.assertEqual(northItem.subItemDetails[("10", "green")].prices.exportPrice, 15)
        self.assertEqual(northItem.subItemDetails[("10", "green")].prices.wholesalePrice, 25)
        self.assertEqual(northItem.subItemDetails[("10", "green")].prices.retailPrice, 50)
        self.assertEqual(northItem.subItemDetails[("10", "green")].prices.currency, "dollar")

if __name__ == '__main__':
    unittest.main()
