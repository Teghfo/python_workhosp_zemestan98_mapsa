from model import User, Product, Comment
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    filename='example.log',
                    level=logging.DEBUG)

logging.warning('hello')
logging.error('hello error')

users = []
products = {}  # {productid: [product, count]}

# def add_product(product, count):
#     if product.id in products.keys():
#         products[product.id][1] + count

#     else:
#         products[product.id] = [product, count]


def remove_product(product, count):
    if product.id not in products.keys():
        print('product not available!')

    elif products[product.id][1] >= count:
        products[product.id][1] -= count

    else:
        print('be andazei ke mikhay nadarim')


def generate_add_product(name, price, seller, category, new_count):
    for product_id, value_products in products.items():
        if value_products[0].name == name:
            value_products[1] += new_count
            return value_products[0]

    new_product = Product(name, price, seller, category)
    products[new_product.id] = [new_product, new_count]
    return new_product


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


def user_comments(username):

    current_user = None
    user_all_comment = []
    for user in users:
        if user.username == username:
            current_user = user
            break

    if current_user:
        for product, count in products.values():
            for comment in product.comments:
                if comment.user == current_user:
                    user_all_comment.append({product.name: comment})

    return user_all_comment


if __name__ == '__main__':
    product1 = generate_add_product('souVaSoun', 5000, 'Masoumeh',
                                    Product._category[0], 12)
    product2 = generate_add_product('GhaleHeivanat', 70000, 'Ali',
                                    Product._category[0], 10)
    product3 = generate_add_product('kash vaghti 20salam boud midanestam',
                                    50000, 'Saeed', Product._category[0], 8)
    product4 = generate_add_product('LG', 50000000000, 'Babak',
                                    Product._category[1], 7)
    product5 = generate_add_product('Royal', 500000, 'Ashkan',
                                    Product._category[3], 6)

    product5 = generate_add_product('Royal', 500000, 'Ashkan',
                                    Product._category[3], 5)

    add_user('ashkan', 912)
    add_user('kasra', 913)
    add_user('zahra', 914)
    add_user('iman', 915)

    buy_product(users[0], product1.id, 4)

    comment1 = Comment(users[0], 4.5, 'merc, kheili khosham umad!')
    comment2 = Comment(users[3], 5, 'nakharidam ama hes mikonam khube!')
    comment3 = Comment(users[0], 4.9, 'merc, kheilewg;hewhgei khosham umad!')
    comment4 = Comment(users[0], 4.2, 'khosham umad!')

    product1.add_comment(comment1)
    product1.add_comment(comment2)
    product2.add_comment(comment3)
    product3.add_comment(comment4)

    show_comments(product1)

    # for comment in user_comments('ashkan'):
    #     for key, value in comment.items():
    #         print(f'{key}  ---- comment: {value.matn}')

    print(products)