l = ['abc', 'fgd', 'loi'] #muttable we caan change the val.
t = ('abc', 'fgd', 'loi') #immutable cant change val.
s = {'abc', 'fgd', 'loi'}  #sets doesnt allow duplicates

print(l[0])
print(t[1])

l[0] = 'def' # update 1st val
# throws error because its immutable  t[1] ='def'
l.append('xyz') #to add element at the end of the list.
# throws error because its immutable  t.append('xyz')
l.remove('abc') # remove given val from list
s.add('vgy') # add elem to set we cant add same element multiple times in set.