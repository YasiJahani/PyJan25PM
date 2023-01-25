
fic=open("numbers.txt")

for line in fic:
    line=line.rstrip()
    print(line)

fic.close()