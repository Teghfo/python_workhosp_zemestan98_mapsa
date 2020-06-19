import unittest

from model import Product
import store

# def sum(a, b):
#     return a + b

# class TrainingTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print('class setup')

#     @classmethod
#     def tearDownClass(cls):
#         print('class tear down')

#     def setUp(self):
#         print('setup executesd')
#         self.a = 10
#         self.b = 5

#     def tearDown(self):
#         print('teardown executed')

#     def test_sum(self):
#         print('test sum')
#         # Arrange
#         a = 5
#         b = 10

#         #act
#         result = sum(a, b)

#         #assert
#         self.assertEqual(result, 15)

#     def test_create_product(self):
#         print('test_create')
#         pass


class ProductTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product('lebas narenji', 1000, 'sakineh',
                              Product._category[2])

    @classmethod
    def tearDownClass(cls):
        del cls.product

    def test_create_object(self):
        self.assertIsInstance(self.product, Product)

    def test_product_attr(self):
        result = self.product.category

        self.assertEqual(result, Product._category[2])


class UserTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
