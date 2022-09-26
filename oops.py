class student:
    def __init__(self):
        self.name = 'rd'
        self.strd = 9
        self.grade = (90,85,98,85,99)

    def average(self):
        return sum(self.grade)/len(self.grade)



std = student()
std.strd
student.average(std) 
std.average()

#another way by pasing parameters

class student1:
    def __init__(self, name, grade):
        self.name = name
        self.strd = 9
        self.grade = grade

    def average(self):
        return sum(self.grade)/len(self.grade)


std1 =student1('rd',(90,85,58,85,99))
std1.average()

#__ str__ and __repr__ methods

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


aksh = person('rd',25)
aksh # it prints objectto overcome use below to print string.

#__str__ method
class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self) :
        return f'{self.name} is {self.age} years old.'

hri = person1('hri', 27)
print(hri)

#__repr__ method

class person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #def __str__(self) :
    #    return f'{self.name} is {self.age} years old.'

    def __repr__(self):
        return f'<person2({self.name}, {self.age})>'

hri = person2('hri', 27)
print(hri)


#Exercise

class Store:
    def __init__(self,name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name=name
        self.items=[]
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item={'name':name,'price':price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total=0
        for i in self.items:
            total+=i['price']
        return total