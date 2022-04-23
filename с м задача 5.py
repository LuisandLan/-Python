a=int(input('введите высоту коробки'))
b=int(input('введите длинну коробки '))
c =int(input('введите ширена коробки'))
m=int(input('введите высоту двери '))
k= int(input('введи ширину двери'))
if b > m and a >m and c > m  and a > k:
    print('коробка не входит в дверь')
elif  m > a and m > b and m > c and k > a:
    print('коробка влезла ')

