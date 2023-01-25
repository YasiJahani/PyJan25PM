
"""
Collection: list, tuple, str, set, dict, array, ....

    Sequences: list, tuple, str, array

    "iterable": len(), sum(), max(), min()
"""
#name="Dave Gahan" # a str
name=[12,3.4,True,"end"] # a list

print(len(name))

for c in name:
    print(c)
    
#name = name + " depeche mode"
name = name + [100, 200]
print(name)

if 3.4 in name:
    print(f"{name} contains the string 3.4")
    
    