'''import math      
def Armstrong(num):
    sum = 0
    num1 = num
    while(num>0):
        sum+=pow((num%10),3)
        num=int(num/10)
    if(sum==num1):
        print('armstrong number')
    else:
        print('not armstrong')
value = input('enter number to check: ')
Armstrong(int(value))
'''
'''
employee = dict()
employee["employee_no"] = input('enter employee no: ')
employee["name"] = input('enter name: ')
employee["basic_pay"] = input('enter basic pay: ')
#employee.get("basic_pay")
if int(employee["basic_pay"])>100000:
    employee["HRA"] = '15%'
    employee["Da"] = '8%'
    employee["Net_pay"] = int(employee["basic_pay"])*0.97
elif int(employee["basic_pay"])<=100000 and int(employee["basic_pay"])>50000:
    employee["HRA"] = '10%'
    employee["Da"] = '5%'
    employee["Net_pay"] = int(employee["basic_pay"])*0.95
else:
    employee["HRA"] = '5%'
    employee["Da"] = '3%'
    employee["Net_pay"] = int(employee["basic_pay"])*0.98
print(employee)
'''

comp1 = 2+5j
comp2 = 3-2j
comp3 = comp1 + comp2
comp4 = comp1*comp2
print(comp3," bhAg ",comp4)    
