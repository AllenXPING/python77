a=int(input(""))
b=[]
for i in range(a):
    b.append(list(map(int,input("").split(" "))))
for i in range(a):
    if b[i][0]%9==0 or b[i][0]%11==0:
        print("第%d個點%d" %(i+1,b[i][0]))
if b[i][0]%9!=0 and b[i][0]%11!=0:
    print("0")