l = [1, 2 ,3]
doubled = [x * 2 for x in l]
doubled

friends = ['vishal', 'saurabh', 'sakhi' ]
starts_s = [friend for friend in friends if friend.startswith('s')]
starts_s

#Dict Key-Val
Dict = {'a': 24, 'b':28, 'c':27 }
Dict['a']
Dict['d'] = 27 #add new key
Dict['a'] =25 # update exixsting key
Dict

friend = [
    {'name' : 'a', 'age': 24},
    {'name' : 'b', 'age': 28},
    {'name' : 'c', 'age': 27}
]
friend[1]


#Destructuring variables
t = (5,11)
x, y = t
print(x,y)

for i in Dict.items():
    print(i)

head, *tail = [1,2,3,4,5]
head
tail

#*head, tail = [1,2,3,4,5]
#head
#tail