import math 
a=int(input('введи сторону а'))
b=int(input('введи сторону b'))
c=int(input('введи сторону c'))
p=1/2*(a+b+c)
S= math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Площадь Герона=',S,'Периметр=',p)