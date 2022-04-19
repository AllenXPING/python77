while True:
    men=int(input("小明身上有幾元:"))
    sell=int(input("販賣機有幾種飲料:"))
    price=[]
    # price1=[]
    flag="False"
    final=0
    if men>100 or men<0:
        break
    if sell>30 or sell<1:
        break
    for i in range(sell):
        price.append(list(map(int,input("多少元").split(" "))))
    # for i in range(len(price)):
    #     for j in range(len(price[0])):
    #         price1.append(price[i][j])
    for i in range(len(price)):
        if price[i][0]>50 or price[i][0]<10:
            flag="True"
            
    if flag=="True":
        break
    for i in range(sell):
        if men >= price[i][0]:
            final+=1
    print(final)
    break
    # print(price)
    # print(price1)
