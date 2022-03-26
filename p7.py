a=(input("輸入月租費形式及通話時間為:"))
a=a.split(",")
b=a[1]
c=0
if a[0] == "186":
   c=int(b)*0.09
   if c <= 186:
       c*=0.9
   elif c>186 :
       c*=0.8 
elif a[0] == "386":
   c=int(b)*0.08
   if c <= 386:
       c*=0.8
   elif c>386 :
       c*=0.7
elif a[0] == "586":
   c=int(b)*0.07
   if c <= 586:
       c*=0.7
   elif c>586 :
       c*=0.6
elif a[0] == "986":
   c=int(b)*0.06
   if c <= 986:
       c*=0.6
   elif c>986 :
       c*=0.5 
d=round(c)
print("通話費為%d" %(d))