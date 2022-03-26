a = input("輸入一整串序列為:")
a=a.split(" ")
b=[]
c=0
total=len(a)/2
for i in a:
    b.append(a.count(i))
d=b.index(max(b))
if int(a[d]) > total:
    print("過半元素為:%s" %(a[d]))
else:
    print("過半元素為:NO")
