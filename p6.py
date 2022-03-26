# a="1,3,9,5,7"
a=input("請輸入值")
a1=a.split(",")
a1.sort()
max=0
min=0
b1=list(map(int,a1))
dight=1*10**((len(a1))-1)
for z in range(len(a1)):
    for j in range(10):
        if j == b1[z]:
            min+=int(j)*dight
    dight/=10

a1.reverse()
b2=list(map(int,a1))
dight=1*10**((len(a1))-1)
for z in range(len(a1)):
    for j in range(10):
        if j == b2[z]:
            max+=int(j)*dight
    dight/=10
print(max-min)