l = [10,20,30,40,50]
print(l)
type(l)
len(l)
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
print(l)

fruits=['apple', 'banana', 'cherry']
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[-3])
print(fruits[-1])
fruits.append('date')
print(fruits)
fruits.remove('banana')
print(fruits)

vegetable = ['vankai', 'bendakai', 'sorakai' ]
print(vegitable)
vegetable.sort()
print(vegetable)

king = ['d','c','b', 'a']
print(king)
king.sort()
print(king)

fruit = ['cherry', 'pineapple', 'banana', 'apple', 'fig']
print(fruit)
fruit.sort()
print(fruit)

part=['kidney', 'liver', 'heart', '']

l=[10,20,30,40,50]
l1=l
print(l1)

l1.clear()
print(l1)

del(l1)
print(l1)

l=[10,20,30,40,-50]
print(l.index(20))
print(l)
print(l.index(40))
print(l.)

l=[10,20,30,40,-50]
print(l.insert(2, 15))


l1=[1,2,3,4,5,6,7]
print(l1)
l2=[2,1,4,3,6,5,7]
print(l2)

l1.sort()
print(l1)

l2.sort()
print(l2)

l1=['a', 'b','Fz', 'd', 'Fa', '1', '#', 'A', 'Z', 'z']
print(l1)
print(sorted(l1))
l2=['b', 'a', 'd', 'c', 'f']
print(l2)
print(sorted(l2))

l=[[1,2,3], [4,5,6], [7,8,9]]
print(l)
print(l[0][-1])
print(l[1][0])

print(id(l))

l=[1, 2, 3, 4, 5]
print(l)
print(100 in l)

#Reverse and sort

l1=[6, 1, 2, 3, 4, 5]
l2=[6,7,8,9,10]
print(l1)
print(l2)

l1.reverse()
print(l1)

l1.sort()
print(l1)
l1.count()
print(l1)


#all and any function
l=[1, 2, 3, 4, []]
print(all(l))
print(any(l))

#all and any function
l=[1, 2, 3, 4, ()]
print(all(l))
print(any(l))

#all and any function
l=[1, 2, 3, 4, {}]
print(all(l))
print(any(l))

#all and any function
l=[1, 2, 3, 4, 0]
print(all(l))
print(any(l))

#all and any function
l=[1, 2, 3, 4, 0.0]
print(all(l))
print(any(l))

#all and any function
l=[1, 2, 3, 4, '']
print(all(l))
print(any(l))

#all and any function
l=[1, 2, 3, 4, None]
print(all(l))
print(any(l))

#all and any function
l=[1, 2, 3, 4, False]
print(all(l))
print(any(l))

print(type("h"))

l=[1, 'A', 1, (1+2j), 1 ]
print(l)
print(l.count(1))

l=[1, 'A', 1, (1+2j), 1, 1 ]
print(l)
print(l.count(1))

l=[1, 'A', 'A', 1, (1+2j), 1, 1 ]
print(l)
print(l.count('A'))

l=[1, 'A', 'A', 1, (1+2j), 1, 1 ]
print(l)
print(l.count(1+2j))