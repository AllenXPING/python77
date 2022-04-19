L=[]
while True:
    L.append(input("請輸入事項(若已無事項，請輸入end):"))
    if "end" in L:
        break
for i in range(len(L)-1):
    print("%d. %s" %(i+1,L[i]))