password = input("請輸入傳送密碼")
list1 = []
if(len(password) != 6):
    print("多餘或少於6位數, 請重新輸入")
else:
    print("密碼為", end="")
    for i in password:
        for j in range(10):
            if(j*4 % 7 == int(i)):
                list1.append(j)
                break
print(list1)