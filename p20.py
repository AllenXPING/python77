a=int(input("組數為:")) 
b=[]
c=1
d=[]
f=0
for i in range(a):
    b.append(list(map(int,(input("第%d組:" %c).split(" ")))))
    c+=1
for j in range(a):
    f=b[j][0]*250+b[j][1]*175
    d.append(f)
for z in range(len(d)):
    print("第%d組應收費用:%d" %(z+1,d[z]) )
    



