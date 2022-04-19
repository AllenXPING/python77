numDict = int(input("輸入筆數"))
listNum = ['金','銀','銅','優']
myDict = {}
for i in range(numDict):
    myDict[listNum[i]] = input("{}".format(listNum[i]))