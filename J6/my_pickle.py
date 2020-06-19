import pickle


class Book:
    def read_data(self):
        self.title = input('Enter Book tile: ')
        if not self.title:
            return
        self.author = input('Enter Author name: ')
        self.page_count = input('Enter page count: ')
        self.borrow_history = []

    def add_borrow_history(self, username):
        self.borrow_history.append(username)

    def print_book_data(self):
        print(f'title: {self.title} author: {self.author} title: {self.title}')


print('----------------------write data-------------------')

f = open('boooooks', 'wb')
book = Book()
book.read_data()

while book.title:
    pickle.dump(book, f)
    book.read_data()

print('all books saved on file boooooks')

f.close()

print('---------------------------read data-------------------')

f = open('boooooks', 'rb')
rogin = pickle.load(f)
print(rogin)

while True:
    rogin.print_book_data()

    try:
        rogin = pickle.load(f)

    except:
        print('Finish!')
        break

print('va TAMAM!')
f.close()