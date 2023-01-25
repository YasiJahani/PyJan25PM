
s={2,3,4,3,12,5,12}
print(s, type(s))

s=set([5,6,7,12,10,6,7])
print(s)

for e in s:
    print(e)
    
s.add(45)
print(s)
# len() sum() max() min() in
s1=set([23,5,7,20,19,15])
s2=s.union(s1)
print(s2)
s2=s.intersection(s1)
print(s2)
s2.pop()
print(s2)