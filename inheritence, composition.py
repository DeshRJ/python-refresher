# inheritance

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False


# printer = Device("Printer", "USB")
# print(printer)

# We don't want to add printer-specific stuff to Device, so...


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # super(Printer, self).__init__(name, connected_by)  - Python2.7
        super().__init__(name, connected_by)  # Python3+
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            raise TypeError("Device is disconnected at this time, cannot print.")
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.print(50)
print(printer)
printer.disconnect()
printer.print(30)  # Error


#composition 
 #Something I see a lot, but you SHOULDN'T DO

#counterpart of inheritence
class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books."


shelf = BookShelf(300)


class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name


# This makes no sense, because now you need to pass `quantity` to a single book:

book = Book("Harry Potter", 120)
print(book)  # What?

# -- Composition over inheritance here --

# Inheritance: "A Book is a BookShelf"
# Composition: "A BookShelf has many Books"


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)