x = float(input("輸入x座標點:"))
y = float(input("輸入y座標點:"))
c = (x*2+y*2)
if x==0 and y==0 :
    print("該點位於原點上")

elif x==0 and y>0 :
    print("該點位於上半平面Y軸上,離原點距離為根號{0}" .format(c))
elif x==0 and y<0 :
    print("該點位於下半平面Y軸上,離原點距離為根號{0}" .format(c))

elif y==0 and x<0 :
    print("該點位於左半平面X軸上,離原點距離為根號{0}" .format(c))
elif y==0 and x>0 :
    print("該點位於右半平面X軸上,離原點距離為根號{0}" .format(c))
elif x>0 and y>0 :
    print("第I象限,離原點距離為根號{0}" .format(c))
elif x>0 and y<0 :
    print("第IV象限,離原點距離為根號{0}" .format(c))
elif x<0 and y>0 :
    print("第II象限,離原點距離為根號{0}" .format(c))
elif x<0 and y<0 :
    print("第III象限,離原點距離為根號{0}" .format(c))