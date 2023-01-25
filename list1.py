# Creation
name=[12,3.4,True,"end"] # a list
print(name)
name=list()
print(name)
print(len(name))
name=list("Maria")
print(name)
name=[12,23,56,67,12,100,200,57]
# info about list: len() type() 
print(len(name), type(name))

# Access to the elements
print("first element", name[0])
print("last element", name[-1])

for c in name:
    print(c)

ix=0
while ix <len(name):
    print(name[ix])
    ix += 1

print(name[1:3])
print(name[3:])
print(name[:4])
print(name[:])
print(name[1::2])
print(name[::-1])
print(name[-7:-5])

# Add, remove, update, ...:
print(name)
name.insert(0,5)
print(name)
name.append(78)
print(name)
name.extend([6,7,8])
print(name)
name.pop(2)
print(name)
name.remove(78)
print(name)
result=name.sort()
print(name)
print(result)

print(sum(name))
print(max(name))

while 12 in name:
    name.remove(12)
    
print(name)



    