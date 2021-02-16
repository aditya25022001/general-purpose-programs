from tabulate import tabulate
headers=["x","y","z","x1","y1","z1"]
rows=[]
x=0
y=0
z=0
steps=8
def xE(vary, varz):
    return round((5+2*vary-varz)/7,4)
def yE(varx, varz):
    return round((-1+3*varx-4*varz)/9,4)
def zE(varx, vary):
    return round(-(2-4*varx+5*vary)/12,4)
while(steps>=0):
    x1=xE(y,z)
    y1=yE(x1,z)
    z1=zE(x1,y1)
    rows.append((x,y,z,x1,y1,z1))
    x,y,z=x1,y1,z1
    steps-=1
print(tabulate(rows,headers=headers))
