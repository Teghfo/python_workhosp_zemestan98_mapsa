from model import User, Product, Comment

users = []
products = {}  # {productid: [product, count]}


def add_product(product, count):
    if product.id in products.keys():
        products[product.id][1] + count

    else:
        products[product.id] = [product, count]


def remove_product(product, count):
    if product.id not in products.keys():
        print('product not available!')

    elif products[product.id][1] >= count:
        products[product.id][1] -= count

    else:
        print('be andazei ke mikhay nadarim')


def generate_product(name, price, seller, category):
    for product in products.keys():
        if product.name == name:
            return product

    return Product(name, price, seller, category)

