a=int(input("班級數:"))
b=[]
c=[]
for i in range(a):
    # b.append(list(map(int,input("每班人數:".split(" "))))) 
    b.append(input("每班人數:".split(" ")))
c=[int(i) for i in b]
final=max(c)
print(final)