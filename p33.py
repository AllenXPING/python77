def LKK(a):
    return round(sum(a)/len(a), 2)


score = []
subject = ["國文", "英文", "微積分", "體育", "程設"]

score.append(int(input("國文")))
score.append(int(input("英文")))
score.append(int(input("微積分")))
score.append(int(input("體育")))
score.append(int(input("程設")))

high_score = max(score)
lowest_score = min(score)
average = LKK(score)

high_index = score.index(high_score)
lowest_index = score.index(lowest_score)

print("平均分數", average,"分")
print("最高分數", subject[high_index], high_score,"分")
print("最低分數", subject[lowest_index], lowest_score,"分")