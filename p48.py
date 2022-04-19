n = int(input("請輸入幾個筆數"))
dicta = {}

for i in range(0, n):
    toAppend = input().split(' ')
    english = toAppend[0]
    chinese = toAppend[1]
    dicta[english] = chinese

query = input("輸入要查詢的單字")
if(query in dicta):
    print(query, "中文意思為", dicta[query])
else:
    print("字典沒有這個資料")