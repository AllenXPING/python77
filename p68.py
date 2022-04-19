ans=input("請輸入第一組數字:")
qes=input("請輸入第一組數字:")


c=0
d=0
for i in range(len(ans)):
    for j in range(len(qes)):
        if qes[i]==ans[j]:
            if i==j:
                c=c+1
            else:
                d=d+1
final=str(c)+'A'+str(d)+'B'
if final=="4A0B":
    print(str(c)+'A'+str(d)+'B',"全對")
else:
    print(str(c)+'A'+str(d)+'B',"加油")
