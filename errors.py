def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


grades = []  # Imagine we have no grades yet
# average = divide(sum(grades) / len(grades))  # Error!

try:
    average = divide(sum(grades), len(grades))
    print(average)
except ZeroDivisionError as e:
    print(e)
    # Much friendlier error message because now we're dealing with it
    # In a "students and grades" context, not purely in a mathematical context
    # I.e. it doesn't make sense to put "There are no grades yet in your list"
    # inside the `divide` function, because you could be dividing something
    # that isn't grades, in another program.
    print("There are no grades yet in your list.")

# -- Built-in errors --

# TypeError: something was the wrong type
# ValueError: something had the wrong value
# RuntimeError: most other things

# Full list of built-in errors: https://docs.python.org/3/library/exceptions.html


# -- Doing something if no error is raised --

grades = [90, 100, 85]

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list.")
else:
    print(f"The average was {average}")


# -- Doing something no matter what --
# This is particularly useful when dealing with resources that you open and then must close
# The `finally` part always runs, so you could use it to close things down
# You can also use it to print something at the end of your try-block if you like.

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")


#custom errors

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python 101", 50)
python101.read(35)
python101.read(50)  # Whaaaat

# -- Errors used to prevent things from happening --


class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python 101", 50)
python101.read(35)
python101.read(
    50
)  # This now raises an error, which has a helpful name and a helpful error message.