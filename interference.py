from random import randint

with open("msg.txt", "r") as f:
    file=f.read()
    
file = file.split("\n")

errX = randint(0,len(file)-2)
errY = randint(0,7)

tempSX = file[errX][:errY]
tempDX = file[errX][errY+1:]
file[errX] = tempSX+"0"+tempDX if file[errX][errY] == "1" else tempSX+"1"+tempDX

with open("msg.txt", "w") as f:
    for r in range(len(file)-1):
        f.write(file[r]+"\n")