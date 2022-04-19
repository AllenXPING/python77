ans=["1","2","3","4"]
qes=[]
while "0000" not in qes:
    qes.append(input("請輸入"))


for i in range(len(qes)-1):
    c=0
    d=0
    for j in range(4):
        if qes[i][j]==ans[j]:
            c=c+1
        elif qes[i][j] in ans:
            d=d+1
                
    final=str(c)+'A'+str(d)+'B'
    print(str(c)+'A'+str(d)+'B')
        

