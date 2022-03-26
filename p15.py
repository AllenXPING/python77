a="1234"
a=list(map(int,a))
for i in range(4):
    a[i]=(a[i]+7)%10
b=0
b=a[0]
a[0]=a[2]
a[2]=b
b=0
b=a[1]
a[1]=a[3]
a[3]=b
print("輸出加密後的數字為:%s" %(a))

