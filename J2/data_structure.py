# list


# my_list = [5, 'ashkan', 5.77, ['akbar', 6], ('asghaar', 5), {'name': 'ashkan'}]
# my_list.append('asgharGholi')
# my_list.insert(3 , 'sakineh')

# my_list2 = my_list.copy()

# my_list.append('Mapsa')
# print(my_list2)
# # my_list.clear
# # print(my_list)

class Khodro():
    def __init__(self, color, charm):
        self.color = color
        self.charkh = 'sport'
        self.charm = charm

    def start(self):
        print("mashin roshan shod!")

    def print_color(self):
        print(self.color)

khodro1 = Khodro('blue', True)
khodro2 = Khodro('red', False)

khodro1.start()
khodro2.print_color()
print(khodro1.charm)


def my_fun(*arg):
    pass




