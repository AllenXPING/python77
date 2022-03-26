# a = input("輸入五張牌")
a="A K 5 9 10"
a=a.split(" ")
x=0
b=[]
for i in range(5):
    if a[i] == "A":
        x += 1
    elif a[i] == "J":
        x += 11
    elif a[i] == "Q":
        x += 12
    elif a[i] == "K":
        x += 13
    else :
        b.append(int(a[i])) 

x+=sum(b)
print(x)

