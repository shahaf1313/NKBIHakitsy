import unittest
from NorthStockItem import *

class TestNorthStock(unittest.TestCase):
    def test_Hakitsy(self):
        x = NorthStockItem("Orbit", "Hakitsy")
        self.assertIsNotNone(x)
        print(x)

if __name__ == '__main__':
    unittest.main()
