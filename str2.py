# Str handling
# [ix] [ix1:ix2] [ix1:ix2:ix3] len() in + 

text="a long line"
print(text)
print(len(text))
print(text[2])

text="---hello------"
print(text.strip("-"))

text="12;67;text.py;jpf@osyx.com;56"
result=text.split(";")
print(result)
text=":".join(result)
print(text)

text=text.replace(":",",")
print(text)

text=text.upper()
print(text)