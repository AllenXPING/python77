a=(list(map(int,input("輸入a n:").split(" "))))
a[0]=a[0]*a[1]
a[1]-=1
print("%dx**%d" %(a[0],a[1]))