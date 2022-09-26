class classtest:
    def instance_method(self):
        print(f'its instance methode of {self}')

    @classmethod
    def class_method(cls):
        print(f'its class methode of {cls}')

    @staticmethod  # dosent have any parameter
    def static_method():
        print('its static methode.')

classtest.static_method()

classtest.class_method()
test =classtest()
test.instance_method()
classtest.instance_method(test)


class book:
    types = ('hardcover', 'paperback')

    def __init__(self, name, booktype, weight):
        self.name = name
        self.booktype = booktype
        self.weight = weight

    def __repr__(self):
        return f'<book {self.name}, {self.booktype}, weighing {self.weight}g>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return book(name, book.types[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return book(name, book.types[1], page_weight)


print(book.types)

bk =book('harry', 'hardcover', 1200)
bk.name

print(bk) #run after repr method

#run after classmethod
bk1 = book.hardcover('Harry', 1200)
print(bk1)

light = book.paperback('python 101',150)
print(light)