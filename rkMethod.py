import math
from tabulate import tabulate
x0=1
y0=-2
alpha=1.4
n=2
h=(alpha-x0)/n
lisK=[]
headers=["k1","k2","k3","k4","k","yact","x"]
def function(x,y):
    return (1+math.log(x)-5*x*y)/(2.5*(x**2))
while(x0<=alpha-h):
    k1=h*function(x0,y0)
    k2=h*function(x0+h/2,y0+k1/2)
    k3=h*function(x0+h/2,y0+k2/2)
    k4=h*function(x0+h,y0+k3)
    k=(k1+2*k2+2*k3+k4)/6
    yact=round(y0+k,10)
    lisK.append((k1,k2,k3,k4,k,yact,x0))
    x0=x0+h
    y0=yact
print(tabulate(lisK,headers=headers))