#we can reuse it many times
def hello():
    print('hello')

hello()

def user_age_in_sec():
    years = int(input('Your age in years : '))
    seconds = years * 60 * 60 * 24  * 365
    print(f'Your age, {years}, is equal to {seconds} seconds.')

user_age_in_sec()

#function arguments and parameter

def add(x,y): #here x and y are called parameters
    return x + y

add(5, 3) #here 5 and 3 are called arguments.

#fun without parameters.
#default parameter val

def sub(x, y=8):
    return x - y

sub(14)

#return value in fun
#return will terminate the fun we can use multiple time when using if else like conditions.


#exercise
# Complete the function by making sure it returns 42. .
def return_42():
    return 42

# Create a function below, called my_function, that takes two arguments and returns the result of its two arguments multiplied together.
def my_function(x, y):
    return x * y


