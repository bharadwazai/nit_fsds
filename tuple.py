#tuple


t1=() # empty tuple
t2=(10,30,60) #integers
t3=(10.77, 30.66, 60.89) #Float
t4=('One', 'two', 'three') #string
t5=('Asif', 25, (50,100), (150,90)) #nested tuple
t6=(100, 'Asif', 17.765)
t7=('Asif', 25, [50,100], [150, 90], {'John', 'David'}, (99, 22,33))

print(len(t7))

# tuple indexing

print(t2[0])
print(t4[0])
print(t4[0][0])
print(t4[-1])

# tuple slicing

mt=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight')
print(mt[0:3])
print(mt[2:5])
print(mt[:2])
print(mt[-3:])
print(mt[-2:])
print(mt[-1])
print(mt[:])

# tuple membership
mt=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight')
print('one' in mt)
print('ten' in mt)

# index position

mt=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight')
print(mt.index('one'))
print(mt.index('five'))

# sorting

mt=(43, 67, 99, 12, 6, 90, 67)
print(sorted(mt))
print(sorted(mt, reverse=True))

# remove & change items
mt = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight')
del mt[0]
print(mt[0])

