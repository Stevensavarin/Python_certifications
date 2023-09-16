import unittest

from product import Product
from shopping_cart import ShoppingCart

from product import ProductDiscountError


def is_available_to_skip():
    return True


class TestShoppingCar(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("El método de clase setUpClass se ejecuta antes de todas las pruebas")


    @classmethod
    def tearDownClass(cls):
        print("El método de clase tearDownClass se ejecuta después de todas las pruebas")
    


    def setUp(self):
       self.name = "iPhone"
       self.price = 500.000
       self.smartphone = Product(self.name, self.price)

       
       self.shopping_cart_1 = ShoppingCart()
       
       self.shopping_cart_2 = ShoppingCart()
       self.shopping_cart_2.add_product(self.smartphone)


    def tearDown(self):
        pass


    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), "Lo sentimos, el carrito de compra no se encuentra vacío.")


    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())


    def test_product_in_shopping_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

        product = Product("Nuevo producto", 10)
        self.shopping_cart_2.add_product(product)

        self.assertIn(self.smartphone, self.shopping_cart_2.products)


    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)


    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name="Example", price=10.0, discount=11.0)


    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name="Libro", price=15.0))
        self.shopping_cart_1.add_product(Product(name="Cámara", price=700, discount=70))

        self.assertGreater(self.shopping_cart_1.total, 0) # >
        self.assertLess(self.shopping_cart_1.total, 1000) # <
        self.assertEqual(self.shopping_cart_1.total, 645.00)
        
        #assertGreaterEqual
        #assertLessEqual


    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0.0)


    @unittest.skip("La prueba no cumple con los requerimientos necesarios")
    def test_skip_example(self):
        self.assertEqual(1, 1)


    @unittest.skipIf(is_available_to_skip(), "No se ecuentra con todos los requerimientos")
    def test_skip_example_two(self):
        pass


    #skipIf -> Evalua sobre Verdadero
    #skipUnless -> Evalua sobre Falso


def test_code_product(self):
    self.assertRegex(self.smartphone.code, self.smartphone.name) #Regex


if __name__ == "__main__":
    unittest.main()