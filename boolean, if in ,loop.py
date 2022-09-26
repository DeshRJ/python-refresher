#boolean
print(5 == 5) 
print(9 > 5)
print(10 != 10)
#comparison : ==, !=, >, <, >=, <= 

# if statement

day_of_week = input('what day of week is it today? ')
print(day_of_week == 'Monday')
if day_of_week == 'Monday':
    print('Have a great start of week.')
else:
    print('full speed ahead.') 
print('it always runs')   


# in keyword

friends = ['a', 'b', 'c', 'd']
print('b' in friends  )

movies = {'kF','TF','PC'}
user_movie = input('enter the movie you watched : ')
print(user_movie in movies)

if user_movie in movies:
    print(f'I have watched {user_movie} too ')
else :
    print('I havent.')


num  = 7
user_input = input('Enter y if you want to play :')
if user_input == 'y':
    user_num = int(input('guess the num: '))
    if user_num == num:
        print('its correct.')
    elif abs(num - user_num) in (1, -1):
        print('you were off by one.')
    else:
        print('its incorrect.')



#loop

num  = 7
user_input = input('would u like to to play? (Y/n)')
while user_input != num:
    user_num = int(input('guess the num:' ))
    if user_num == num:
        print('its correct.')
    elif abs(num - user_num) in (1, -1):
        print('you were off by one.')
    else:
        print('its incorrect.')

    user_input = input('would u like to to play? (Y/n)')


#another way 
#while true always put in infinite loop so you have to terminate it within the loop
while True:
    ser_input = input('would u like to to play? (Y/n)')

    if user_input == 'n':
        break

    user_num = int(input('guess the num:' ))
    if user_num == num:
        print('its correct.')
    elif abs(num - user_num) in (1, -1):
        print('you were off by one.')
    else:
        print('its incorrect.')

    user_input = input('would u like to to play? (Y/n)')


friends = ['a', 'b', 'c', 'd']
for i in friends:
    print(f'{i} is my friend.')


grades = [35, 67, 98, 100, 100 ]
total = 0
amount =len(grades)

for i in grades:
    total += i
print(total / amount)


#OR
#grades = [35, 67, 98, 100, 100 ]
#total = sum(grades)
#amount =len(grades)
#print(total / amount)

#Exercise
"""1.Modify the code so that the evens list contains only the even numbers of the numbers list. You do not need to print anything.

For part 2, add a clause to the if statement such that if the user's input is "q", your program prints "Quit"."""
# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number%2 == 0:
        evens.append(number)

user_input = input('enter :')
if user_input == 'a':
    print('Add')
elif user_input == 'q':
    print('Quit')
