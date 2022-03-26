l=[1,4,2,4,2,2,5,2,6,3,3,6,3,6,6,3,3,3,7,8,9,8,7,0,7,1,2,4,7,8,9]
count_times = []
for i in l :
    count_times.append(l.count(i))
    m = max(count_times)
    n = l.index(m)
print (l[n])