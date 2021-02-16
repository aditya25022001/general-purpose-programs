import math
from tabulate import tabulate
headers = ["xk","fk","f`k","xk1","fk1"]
rows = []
lis = []
def function1(var):
    return 3*var-math.cos(var)-1
def functionDiff(var):
    return 3+math.sin(var)
for i in range(-7,7):
    function = function1(i)
    lis.append((function,i))
for i in range(len(lis)-1):
    if lis[i][0]>0 and lis[i+1][0]<0 or lis[i][0]<0 and lis[i+1][0]>0:
        a, b = lis[i][1], lis[i+1][1]
        break
x = a if abs(a-math.e**(-math.sin(a)))<abs(b-math.e**(-math.sin(b))) else b
app = x-0.600 if x<0 else x+0.600
lisk1=[]
lisk1.append(0)
lisk1.append(1)
functionFuture=0
while round(lisk1[len(lisk1)-1],6)-round(lisk1[len(lisk1)-2],6)!=0:
    func = round(function1(app),6)
    funcD = round(functionDiff(app),6)
    xk1 = round((app-(func/funcD)),6)
    functionFuture = round(function1(xk1),6)
    rows.append((app,func,funcD,xk1,functionFuture))
    lisk1.append(xk1)
    app = xk1
print(lisk1[2:len(lisk1)])
print(tabulate(rows,headers=headers))
