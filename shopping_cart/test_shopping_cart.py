import unittest
from unittest.main import main
from shopping_cart import Item, ShoppingCart, NotExistItemError


class TestShoppingCart(unittest.TestCase):

    # despues de las prueba unitaria
    def setUp(self):
        print('despues de las prueba unitaria')
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    # despues de las prueba unitaria
    def tearDown(self):
        pass

    def test_cinco_mas_cinco(self):
        assert 5 + 5 == 10

    def test_nombre_producto_igual_pan(self):
        # comparar dos valores
        # usando el singo igual dos veces
        self.assertEqual(self.pan.name.lower(), "pan")

    def test_nombre_producto_no_igual_pan(self):
        self.assertNotEqual(self.jugo.name.lower(), "pan")

    def test_contiene_producto(self):
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        # dos objetos son iguales
        # palabra reservada "is"
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo)

    def test_excepcion_al_obtener_jugo(self):
        with self.assertRaises(NotExistItemError):
            self.shopping_cart.get_item(self.jugo)



if __name__ == "__main__":
    unittest.main()
