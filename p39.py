import math


n=int(input("輸入整數n:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
        
    for m in range(2*i+1):
        print("*",end="")
    print('')
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
        
    for m in range(2*(n-i)-3):
        print("*",end="")
    print('')