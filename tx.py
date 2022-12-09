stringa = input("Input a string: ")
codice = []
codework = []
conto = 0
bit = 0

for c in stringa:
    c=bin(ord(c))
    codice.append(c)
    
for c in codice:
    vettTemp = []
    c=c[2:]
    if len(c) != 7:
        c = "0"+c
    c = "0"+c if c.count("1")%2==0 else "1"+c
    codework.append(c)
    
codework.append("")
for b in range(8):
    conto = 0
    for i in range(len(codework)-1):
        conto = conto+1 if codework[i][b]=="1" else conto
    codework[len(codework)-1] += "1" if conto%2==1 else "0"
    
with open("msg.txt","w") as f:
    for c in codework:
        f.write(c+"\n")
    f.close()