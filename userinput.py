name  =  input('Enter your name: ')
print(name)

size_input = input('House in sq ft: ')
sq_ft = int(size_input)
sq_met = sq_ft / 10.8
print(sq_met)
print(f'{sq_ft} square feet is {sq_met:.2f} square meters')



# 
years = int(input('Your age in years : '))
months = years * 12
seconds = years * 60 * 60 * 24  * 365
print(f'Your age, {years}, is equal to {months} months.')
print(f'Your age, {years}, is equal to {seconds} seconds.')