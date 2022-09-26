from calendar import MONDAY


name = 'bob'
greetings = ' hello, bob '
print(greetings)
greetings_update = f'Hello, {name}'
print(greetings_update)
name = 'Rohan'
print(greetings_update) #doesnt work if we changed the name value 
#so instead of print(greetings_update) use print(f'Hello, {name}')
print(f'Hello, {name}')


name = 'abc'
greeting = 'Hello, {}'
with_name = greeting.format(name)
print(with_name)

longer_phrase = 'Hello, {}. Today is {}.'
formatted = longer_phrase.format('Aksh' , 'MONDAY')
print(formatted)