a=int(input("請輸入西元年"))
b=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
c=a%12
c-=4
if c < 0 :
    c+=12
print(b[c])