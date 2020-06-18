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


def add_user(username, tel):
    for user in users:
        if user.username == username:
            print('user ro darim! boro login kon!')
            return

    users.append(User(username, tel))


def buy_product(user, product_id, count):
    if product_id not in products.keys():
        print('in kala nadarim!')

    elif products[product_id][1] < count:
        print(
            f'inghadi ke mikhay nadarim. inghad {products[product_id][1]} darim'
        )
    else:
        user.purchase_history.append(products[product_id][0])
        products[product_id][1] - count
        print('kharid anjam shod')


def show_comments(product):
    if product.id not in products.keys():
        print('in kala ra nadarim')

    else:
        for comment in product.comments:
            print(comment.user.username, 'rate: ', comment.rate, 'matnesham: ',
                  comment.matn)


if __name__ == '__main__':
    product1 = generate_product('souVaSoun', 5000, 'Masoumeh',
                                Product._category[0])
    product2 = generate_product('GhaleHeivanat', 70000, 'Ali',
                                Product._category[0])
    product3 = generate_product('kash vaghti 20salam boud midanestam', 50000,
                                'Saeed', Product._category[0])
    product4 = generate_product('LG', 50000000000, 'Babak',
                                Product._category[1])
    product5 = generate_product('Royal', 500000, 'Ashkan',
                                Product._category[3])

    add_product(product1, 12)
    add_product(product2, 2)
    add_product(product3, 6)
    add_product(product4, 9)

    add_user('ashkan', 912)
    add_user('kasra', 913)
    add_user('zahra', 914)
    add_user('iman', 915)

    buy_product(users[0], product1.id, 4)

    comment1 = Comment(users[0], 4.5, 'merc, kheili khosham umad!')
    comment2 = Comment(users[3], 5, 'nakharidam ama hes mikonam khube!')

    product1.add_comment(comment1)
    product1.add_comment(comment2)

    show_comments(product1)