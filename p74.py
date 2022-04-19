ans = ['red', 'blue', 'red', 'green']
list1 = input("輸入顏色").split(" ")
a = b = c = d = 0

if(ans[0] == list1[0]):
    a = 1
elif(list1[0] in ans):
    a = 2
else:
    a = 3

if(ans[1] == list1[1]):
    b = 1
elif(list1[1] in ans):
    b = 2
else:
    b = 3

if(ans[2] == list1[2]):
    c = 1
elif(list1[2] in ans):
    c = 2
else:
    c = 3

if(ans[3] == list1[3]):
    d = 1
elif(list1[3] in ans):
    d = 2
else:
    d = 3
print("{}{}{}{}".format(a, b, c, d))