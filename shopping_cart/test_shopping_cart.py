import unittest
from unittest.main import main
from shopping_cart import Item, ShoppingCart


class TestShoppingCart(unittest.TestCase):

    # despues de las prueba unitaria
    def setUp(self):
        print('despues de las prueba unitaria')
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)
        self.shopping_cart = ShoppingCart()

    # despues de las prueba unitaria
    def tearDown(self):
        pass

    def test_cinco_mas_cinco(self):
        assert 5 + 5 == 10

    def test_nombre_producto_igual_pan(self):
        self.assertEqual(self.pan.name.lower(), "pan")

    def test_nombre_producto_no_igual_pan(self):
        self.assertNotEqual(self.jugo.name.lower(), "pan")


if __name__ == "__main__":
    unittest.main()
