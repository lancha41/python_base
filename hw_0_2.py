import math
a=int(input('Enter first side of triangle: '))
b=int(input('Enter second side of triangle: '))
c=int(input('Enter third side of triangle: '))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Area of triangle:',s)


