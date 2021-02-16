import math
from tabulate import tabulate
headers = ["ak", "bk", "f(ak)", "f(bk)", "xk+1", "f(xk+1)"]
rows= []
lis=[]
a,b=0,0
print(-1*(math.pow(math.e,-1))-math.sin(-1))
def function1(var):
    return (var**2)+(math.e**var)*math.cos(var)+math.log(var**2+2)-3
for i in range(-5,5):
    function = function1(i)
    lis.append((function,i))
print(lis)
for i in range(len(lis)-1):
    if lis[i][0]>0 and lis[i+1][0]<0 or lis[i][0]<0 and lis[i+1][0]>0:
        a,b=lis[i][1],lis[i+1][1]
        break
print("root lies in : ("+str(a)+","+str(b)+")")

lisk1=[]
lisk1.append(0)
lisk1.append(1)
while round(lisk1[len(lisk1)-1],4)-round(lisk1[len(lisk1)-2],4)!=0:
    funak = function1(a)
    funbk = function1(b)
    xk1 = (a*funbk-b*funak)/(funbk-funak)
    funxk1 = function1(xk1)
    rows.append((a,b,funak,funbk,xk1,funxk1))
    lisk1.append(xk1)
    if funxk1>0 and funak<0 or funxk1<0 and funak>0:
        a,b = a,xk1
    if funxk1>0 and funbk<0 or funxk1<0 and funbk>0:
        a,b = xk1,b
print(lisk1[2:])
print(tabulate(rows,headers=headers))
print(xk1)
print(((-1.3211)**2)+(math.e**(-1.3211))*math.cos(-1.3211)+math.log((-1.3211)**2+2)-3)