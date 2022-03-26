a= input("第一個矩陣列行:")
a=a.split(" ")
b=[]
c=[]
for i in range(int(a[0])):
    b.append(input("第一個矩陣第%d列的值" %(i+1)))
for z in range(int(a[0])):
    c.append(b[z].split(" "))

a2 = input("第二個矩陣列行:")
a2=a2.split(" ")
b2=[]
c2=[]
tota=[]
ct=[]
ct2=[]
o=0
for j in range(int(a2[0])):
    b2.append(input("第二個矩陣第%d列的值" %(j+1)))
for x in range(int(a[0])):
    c2.append(b2[x].split(" "))
if a != a2:
    print("兩個矩陣無法相加")
elif a == a2:
    for n in range(int(a[0])):
        ct.append(list(map(int,c[n])))
        ct2.append(list(map(int,c2[n])))
    
    for v in range(int(a[0])):
        for b in range(int(a[1])):
            tota.append(ct[v][b] + ct2[v][b])
for m in range(int(a[0])):
    for h in range(int(a[1])):
        print(tota[o] ,end=" ")
        o+=1
    print()
