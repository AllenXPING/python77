a=int(input("測試的資料量:"))
# a=2
a2=[]
b=[]

for i in range(a):
    a2.append(input("輸入血型:"))
    # a2.append("O O O")
for j in range(a):
    b.append((a2[j].split(" ")))
for n in range(a):
    if (b[n][0]=="O" or b[n][1]=="O")and(b[n][1]=="O" or b[n][0]=="O"):
        if b[n][2]=="O":
            print("YES")
        elif b[n][2]!="O":
            print("IMPOSSIBLE")

    elif (b[n][0]=="O" )and(b[n][1]=="A"):
        if b[n][2]=="O"or b[n][2]=="A":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="A":
            print("IMPOSSIBLE")
        
    elif (b[n][0]=="A" )and(b[n][1]=="O"):
        if b[n][2]=="O"or b[n][2]=="A":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="A":
            print("IMPOSSIBLE")

    elif (b[n][0]=="O" )and(b[n][1]=="B"):
        if b[n][2]=="O"or b[n][2]=="B":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="B":
            print("IMPOSSIBLE")
    elif (b[n][0]=="B" )and(b[n][1]=="O"):
        if b[n][2]=="O"or b[n][2]=="B":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="B":
            print("IMPOSSIBLE")

    elif (b[n][0]=="O" )and(b[n][1]=="AB"):
        if b[n][2]=="A"or b[n][2]=="B":
            print("YES")
        elif b[n][2]!="A" or b[n][2]!="B":
            print("IMPOSSIBLE")
    elif (b[n][0]=="AB" )and(b[n][1]=="O"):
        if b[n][2]=="A"or b[n][2]=="B":
            print("YES")
        elif b[n][2]!="A" or b[n][2]!="B":
            print("IMPOSSIBLE")
    
    elif (b[n][0]=="A" )and(b[n][1]=="A"):
        if b[n][2]=="O"or b[n][2]=="A":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="A":
            print("IMPOSSIBLE")
        
    
    
    elif (b[n][0]=="A" )and(b[n][1]=="B"):
        if b[n][2]!="O" or b[n][2]!="A" or b[n][2]!="B" or b[n][2]!="AB":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="A" or b[n][2]!="B" or b[n][2]!="AB":
            print("IMPOSSIBLE")
    elif (b[n][0]=="B" )and(b[n][1]=="A"):
        if b[n][2]!="O" or b[n][2]!="A" or b[n][2]!="B" or b[n][2]!="AB":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="A" or b[n][2]!="B" or b[n][2]!="AB":
            print("IMPOSSIBLE")

    elif (b[n][0]=="A" )and(b[n][1]=="AB"):
        if b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("YES")
        elif b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("IMPOSSIBLE")
    elif (b[n][0]=="AB" )and(b[n][1]=="A"):
        if b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("YES")
        elif b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("IMPOSSIBLE")

    elif (b[n][0]=="B" )and(b[n][1]=="B"):
        if b[n][2]=="O"or b[n][2]=="B":
            print("YES")
        elif b[n][2]!="O" or b[n][2]!="B":
            print("IMPOSSIBLE")
        
        
        
    

    elif (b[n][0]=="B" )and(b[n][1]=="AB"):
        if b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("YES")
        elif b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("IMPOSSIBLE")
    elif (b[n][0]=="AB" )and(b[n][1]=="B"):
        if b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("YES")
        elif b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("IMPOSSIBLE")

    elif (b[n][0]=="AB" )and(b[n][1]=="AB"):
        if b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("YES")
        elif b[n][2]!="AB" or b[n][2]!="A" or b[n][2]!="B":
            print("IMPOSSIBLE")
        
    



