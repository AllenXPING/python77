a=input("請輸入string_a:")
b=input("請輸入string_b:")
c=[]
d=[]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c.append(a[i])
for i in range(len(c)):
    if c[i] not in d:
        d.append(c[i])
d.sort()
final="".join(d)

if c==[]:
    print("N")
else:
    print(final)
