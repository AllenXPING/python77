list1 = []
for i in range(10):
    list1.append(input("輸入第{}個數字".format(i)))
list2 = sorted(list1, reverse=True)
print("最大的三個數字為：", list2[0], ",", list2[1], ",", list2[2])
print("最小的三個數字為：", list2[-1], ",", list2[-2], ",", list2[-3])