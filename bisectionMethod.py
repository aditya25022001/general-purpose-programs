import math
from tabulate import tabulate
headers=["k","ak","bk","f(ak)","f(bk)","xk","f(xk)"]
rows=[]
lis=[]
k=0
def function1(var):
    return (var**3)-4*var-9
for i in range(1,5):
    function=function1(i)
    lis.append((function,i))
for i in range(len(lis)-1):
    if lis[i][0]>0 and lis[i+1][0]<0 or lis[i][0]<0 and lis[i+1][0]>0:
        a,b=lis[i][1],lis[i+1][1]
        break
print("root lies in : ("+str(a)+","+str(b)+")")
lisk1=[]
lisk1.append(0)
lisk1.append(1)
while round(lisk1[len(lisk1)-1],6)-round(lisk1[len(lisk1)-2],6)!=0:
    funak=function1(a)
    funbk=function1(b)
    xk1=(a+b)/2
    funxk1=function1(xk1)
    rows.append((k,a,b,funak,funbk,xk1,funxk1))
    k+=1
    lisk1.append(xk1)
    if funxk1>0 and funak<0 or funxk1<0 and funak>0:
        a,b = a,xk1
    if funxk1>0 and funbk<0 or funxk1<0 and funbk>0:
        a,b = xk1,b
print(lisk1[2:])
print(tabulate(rows,headers=headers))