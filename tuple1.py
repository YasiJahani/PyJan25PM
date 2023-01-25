# Creation
name=(12,3.4,True,"end") # a tuple
print(name)
name=12,3.4,True,"end" # a tuple
print(name)
name=(12,)
print(name, len(name))
name=tuple("Maria")
print(name)

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

name=(12,3.4,34,67,9)
print(sum(name))
print(max(name))




    