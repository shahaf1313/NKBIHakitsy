import unittest
from src.NorthStockItem import *
from src.StockState import *


class TestNorthStock(unittest.TestCase):
    def test_AddStockItemPrices(self):
        orbit = NorthStockItem("Orbit")
        pulse = NorthStockItem("Pulse")
        self.assertIsNotNone(orbit)
        self.assertIsNotNone(pulse)
        orbitPrice = Prices(10, 15, 25, 50, "dollar")
        pulsePrice = Prices(13, 18, 28, 53, "dollar")
        orbit.updateStockItemPrices("10", "green", orbitPrice)
        orbit.updateStockItemPrices("10", "red", orbitPrice)
        pulse.updateStockItemPrices("10", "green", pulsePrice)
        pulse.updateStockItemPrices("10", "red", pulsePrice)
        self.assertIs(isinstance(orbit.size_color_dict[("10", "green")].prices, Prices), True)
        self.assertEqual(orbit.size_color_dict[("10", "green")].prices.farEastPrice, 10)
        self.assertEqual(orbit.size_color_dict[("10", "green")].prices.exportPrice, 15)
        self.assertEqual(orbit.size_color_dict[("10", "green")].prices.wholesalePrice, 25)
        self.assertEqual(orbit.size_color_dict[("10", "green")].prices.retailPrice, 50)
        self.assertEqual(orbit.size_color_dict[("10", "green")].prices.currency, "dollar")

if __name__ == '__main__':
    unittest.main()
