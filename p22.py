a=int(input("組數為:")) 
b=[]
c=[["123","456"],["456","789"],["789","888"],["336","558"],["775","666"],["566","221"]]
for i in range(a):
    b.append(input().split(" "))
for i in range(a):
    if b[i][0] ==c[0][0]:
        if b[i][1] == c[0][1]:
            print("9000")
        else:
            print("error")
    elif b[i][0] ==c[1][0]:
        if b[i][1] == c[1][1]:
            print("5000")
        else:
            print("error")
    elif b[i][0] ==c[2][0]:
        if b[i][1] == c[2][1]:
            print("6000")
        else:
            print("error")
    elif b[i][0] ==c[3][0]:
        if b[i][1] == c[3][1]:
            print("10000")
        else:
            print("error")
    elif b[i][0] ==c[4][0]:
        if b[i][1] == c[4][1]:
            print("12000")
        else:
            print("error")
    elif b[i][0] ==c[5][0]:
        if b[i][1] == c[5][1]:
            print("7000")
        else:
            print("error")
    else:
        print("error")








