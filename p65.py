a=input("請輸入A的好友:").split(" ")
b=input("請輸入B的好友:").split(" ")
total=0
if len(a)>len(b):
    for i in range(len(a)):
        if a[i] in b:
            total+=1
elif len(a)<len(b):
    for i in range(len(b)):
        if b[i] in a:
            total+=1
print(total)
