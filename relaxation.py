from tabulate import tabulate
headers=["x","y","z","Rx","Ry","Rz"]
rows=[]
rs=[]
x=0
y=0
z=0
Rx=1
Ry=1
Rz=1
steps=11
def RxE(varx, vary, varz):
    return round(-8-4*varx+4*vary-3*varz,4)
def RyE(varx, vary, varz):
    return round(11-3*varx-9*vary+2*varz,4)
def RzE(varx, vary, varz):
    return round(24-4*varx-2*vary-13*varz,4)
def Rxd(var):
    return var/4
def Ryd(var):
    return var/9
def Rzd(var):
    return var/13
while(steps>=0):
    Rx=RxE(x,y,z)
    Ry=RyE(x,y,z)
    Rz=RzE(x,y,z)
    rows.append((x,y,z,Rx,Ry,Rz))
    rs.append(abs(Rx))
    rs.append(abs(Ry))
    rs.append(abs(Rz))
    maximum=max(rs)
    index = rs.index(maximum)
    if index==0:
        x=round(x+Rxd(Rx),4)
    if index==1:
        y=round(y+Ryd(Ry),4)
    if index==2:
        z=round(z+Rzd(Rz),4)
    rs=[]
    steps-=1
print(tabulate(rows,headers=headers))
print(-8-4*(-1.3622)+4*2.0856-3*1.944)
