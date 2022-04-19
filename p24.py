a=int(input("請輸入陣列大小:")) 
b=[]
# b=[[1,3],[2,4]]
c=[]

# z=[]
# zz=[]
for i in range(a):
    b.append(list(map(int,(input().split(" ")))))
for i in range(len(b)):
    for j in range(len(b)):
        c.append(b[i][j])
c.sort()
c.reverse()
# print(c)
total=c[0]+c[1]+c[2]
print("最大值為:%d" %(total)) 
print("位置為:" ,end="")
for h in range(3):
    for i in range(len(b)):
        for j in range(len(b)):
            if c[h] == b[i][j]:
                print("(%d,%d)" %(i+1,j+1) ,end=" ")
# print(c)
# for i in range(len(b)):
#     zz.append(b[z].index(c[i]))



# print(z)
# print(zz)




