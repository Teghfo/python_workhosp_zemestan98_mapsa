class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def add_elem_begin(self, elem):
        if self.root == None:
            self.root = elem
        else:
            elem.next = self.root
            self.root = elem

    def add_elem_end(self, elem):
        pass

    def add_between(self, elm, new_elm):
        pass

    def remove_elm(self, elm):
        pass

    def print_linked_list(self):
        if self.root == None:
            print('Empty')
        else:
            temp = self.root
            while temp:
                print(temp.data)
                temp = temp.next

    def reverse_linked_list(self):
        pass


l = LinkedList()

elm1 = Element('ashkan')
elm3 = Element('roghaieh')
elm2 = Element('farmun')

l.add_elem_begin(elm1)
l.add_elem_begin(elm2)
l.add_elem_begin(elm3)
l.print_linked_list()