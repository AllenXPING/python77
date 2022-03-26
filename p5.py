a=float(input("請輸入M?"))
n=1
s=1
while s<a:
    n+=1
    s*=n
print("超過M為1000的最小階層N值為%d" %(n))