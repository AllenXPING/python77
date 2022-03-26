a=input("輸入月即日為:")
a=a.split(" ")
m=int(a[0])
d=int(a[1])
if m==1 and d>20 or m==2 and d<19:
    print("星座為:Aquarius")
elif m==2 and d>18 or m==3 and d<21:
    print("星座為:Pisces")
elif m==3 and d>20 or m==4 and d<21:
    print("星座為:Aries")
elif m==4 and d>20 or m==5 and d<22:
    print("星座為:Taurus")
elif m==5 and d>21 or m==6 and d<22:
    print("星座為:Gemini")
elif m==6 and d>21 or m==7 and d<23:
    print("星座為:Cancer")
elif m==7 and d>22 or m==8 and d<24:
    print("星座為:Leo")
elif m==8 and d>23 or m==9 and d<24:
    print("星座為:Virgo")
elif m==9 and d>23 or m==10 and d<24:
    print("星座為:Libra")
elif m==10 and d>23 or m==11 and d<23:
    print("星座為:Scorpio")
elif m==11 and d>22 or m==12 and d<22:
    print("星座為:Sagittarius")
elif m==12 and d>21 or m==1 and d<21:
    print("星座為:Capricorn")