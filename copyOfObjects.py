
l1=[5,6,7]

l2=l1

l2.append(100)

print(l1)

print(l1,id(l1))
print(l2,id(l2))

#l2=l1.copy()
l2=l1[:]

l2.append(100)

print(l1)

print(l1,id(l1))
print(l2,id(l2))

