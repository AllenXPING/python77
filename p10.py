a=input("輸入N及M為:")
b=input("輸入矩陣數值第1列為:")
c=input("輸入矩陣數值第2列數值為:")
a=a.split(" ")
b=b.split(" ")
c=c.split(" ")
for i in range(int(a[1])):
    if a[0] =="0"or a[1]=="0":
        break 
    else: 
        d= b[i]+' '+c[i]
        print("輸出矩陣數值第%s列為:%s" %(i+1,d))

