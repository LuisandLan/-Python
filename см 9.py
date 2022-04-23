m=int(input('введи номер билета не больше 54  '))
if m >40 :
    print('боковое')
else:
     print('купе')
if m % 2 == 0:
    print('верхне')
else :
    print('нижнее')