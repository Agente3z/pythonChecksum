with open("msg.txt", "r") as f:
    file=f.read()
    
file = file.split("\n")

pos = 0

for r in file:
    if r.count("1")%2!=0:
        errX = pos
    pos+=1
    
pos = 0
for b in range(8):
    conto = 0
    for i in range(len(file)-1):
        conto = conto+1 if file[i][b]=="1" else conto
    if conto%2!=0:
        errY = pos
    pos+=1

try:
    tempSX = file[errX][:errY]
    tempDX = file[errX][errY+1:]
    file[errX] = tempSX+"0"+tempDX if file[errX][errY] == "1" else tempSX+"1"+tempDX
except:
    pass
   
messaggio = ""
for r in range(len(file)-2):
    r = "0"+file[r][1:]
    totale=0
    for x in range(0,len(r)):
        peso=2**(len(r)-x-1)
        totale+=int(r[x])*peso
    messaggio+=chr(totale)
    
print(messaggio)
input()