import uuid


class User:
    def __init__(self, username, tel):
        self.username = username
        self.age = None
        self.tel = tel
        self.address = None
        self.image = None
        self.purchase_history = []
        self.status = False  # ordinary user


class UserAdmin(User):
    def __init__(self, username, tel, passw):
        super().__init__(username, tel)
        self.status = True
        self.passw = passw


class Product:
    _id = 1000

    _category = ['Book', 'Home_appliance', 'accessories', 'lavazem_arayeshi']

    def __init__(self, name, price, seller, category):
        self.id = Product.id_gen()
        self.serial_num = uuid.uuid4()
        self.name = name
        self.price = price
        self.comments = []
        self.seller = seller
        self.category = category

    def add_comment(self, comment):
        self.comments.append(comment)

    @staticmethod
    def id_gen():
        Product._id += 1
        return Product._id


class Comment:
    def __init__(self, user, rate, matn):
        self.user = user
        self.rate = rate
        self.matn = matn
