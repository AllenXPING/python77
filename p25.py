A=list(map(int,input("考試次數 學生數:").split(" ")))
B=list(map(float,input("考試所佔比率:").split(" ")))
# A=[1,1]
# B=[0.1]
C=[]
# C=[50]
F=[]
D=[]
z=0
for i in range(A[1]):
    C.append(list(map(int,input("第%d個學生的每個分數:" %(i+1)).split(" "))))
    # C+=input("第%d個學生的每個分數:" %(i+1)).split(" ")
# for i in range(len(C)):
#     for j in range(len(C[0])):
#         D.append(C[i][j])
for i in range(A[1]):
    for j in range(A[0]):
        F.append(C[i][j]*(B[j]))
zz=sum(F)/A[1]
print(round(zz,2))





