a = int(input("輸入一個正整數"))
b = []
for i in range(2,a+1):
    if i%2 !=0:
        b.append(i)
b.sort()
b.reverse()
print(b[0])



