f = open("books.txt","r",encoding="utf-8")

k = f.read()
k = k.split("\n----\n")
for i in range(0,len(k)-1):
    k[i]= k[i].split("\n")
    k[i][3] = int(k[i][3])
k.pop(-1)

print(k)