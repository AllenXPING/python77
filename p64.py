x=int(input("請輸入第一個要判斷的數字:"))
z=int(input("請輸入第二個要判斷的數字:"))
x1=x+2
z1=z+2
i = 0
i1=0
o = 0
o1 = 0
yesno=0
yesno1=0
for n in range(2,x):
    if x % n == 0 :
        i = n
for n in range(2,x1):
    if x1 % n == 0 :
        i1 = n
if (i==i1==0):
    yesno=1
else:
    yesno=0

for n in range(2,z):
    if z % n == 0 :
        o = n
for n in range(2,z1):
    if z1 % n == 0 :
        o1 = n
if (o==o1==0):
    yesno1=1
else:
    yesno1=0

if yesno==yesno1==1:
    print("Y")
else :
    print("N")
