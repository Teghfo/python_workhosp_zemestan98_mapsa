x = 5
my_list = [2, 2, 8, 'ashkan']


def f(arg, x):
    # global x
    # arg += 5
    # arg = ['mapsa']
    x += 5
    arg.append(10)
    print(my_list)
    


class A:
    def __init__(self):
        self.x = 14
        
    def khalghezi(self):
        x = 12
        print(x)

a = A()


f(my_list, x)
print(x)
print(my_list)
