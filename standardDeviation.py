import math
array = []
array2 = []
'''Xbar = 12.1
Ubar = 11.7
array = [12.2,11.9,12.5,12.3,11.6,11.7,12.2,12.4]
avg = sum(array)/len(array)
n = 7
deviationSquare = [(x-avg)*(x-avg) for x in array ]
sumdev = sum(deviationSquare)
s = math.sqrt(sumdev/7)
t=(Xbar-Ubar)/(s/math.sqrt(n))
print(t,array,avg,deviationSquare,sumdev,s,sep='\n')'''
def function(each):
    xsq = each**each
    x2 = 2*each
    e2x = pow(math.e,x2)
    lnx = math.log(each)
    prd = e2x*lnx
    return math.sqrt(xsq+prd)
for i in range(1,13):
    array.append(round(i*math.pi/24,2))
print(array)
for each in array:
    array2.append(function(each))
print(array2)