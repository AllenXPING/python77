a=int(input("輸入第一行正整數為:"))
b=(input("輸入第二行中數列中的數字為:"))      

b=b.split(" ")
c=[]
d=0
for i in b:
    c.append(b.count(i))
e=c.index(max(c))
if max(c) == 1:
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數的數字為:%s" %(b[e]))
    print("出現次數為:%s" %(max(c)))
