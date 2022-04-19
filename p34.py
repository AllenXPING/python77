a=int(input("輸入一正整數:"))
if a%2==0 and a%11==0:
    if a%5==0 or a%7==0:
        print("NO")
    else:
        print("YES")
else:
    print("NO")