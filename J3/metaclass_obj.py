# review  ..... module, package, pip, virtualenv, scope, methode type in class


class A:

    _count = 0  # class attribute, static property

    __age = 25  # private attribute

    def __my_private():  #private methode
        A._count += 1

    def __init__(self, name):
        self.name = name
        self.age = 26
        A._count = A.__age
        A.__my_private()

    def print_age(self):
        print(self.age)

    def print_name(self, age):  #instance(object) method
        print(f'{self.name}: {age}')

# static method    ---> 1. arguman ejbari nadare   2. dakhel object copy nemishan  3. be attribute ha dastresi nadaran

    @staticmethod  ### decorator
    def object_count():
        print(A._count)


# class method  ---> 1. arguman ejbarishun class mibashad.

    @classmethod
    def my_new(cls):
        if cls._count < 4:
            print('kheili bachei')
        else:
            print('dg bozorg shodi')

a = A('Saeed')

# b = A('Sakineh')
# c = A('Sakineh')
# c = A('Sakineh')

# a.print_name()
# b.print_name()

# A.object_count()

# print(a._count)
# print(b._count)

# A.my_new()
# A.my_new_static()


# inheritance   ----> all public methode and attribute inheritanced
class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def print_name(self):  # override
        super().print_name()
        print(f'helllo jenab {self.name} , senesh {self.age}')

    def print_in_b(self):
        pass


class C:
    def __init__(self):
        self.name = 'asghar'

    def print_name(self):
        print(self.name)


class D(C, A):
    pass


# b_obj = B('kasra', 40)
# b_obj.print_name()
# print(b_obj.__age)

d_obj = D()
d_obj.print_age()