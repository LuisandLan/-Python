N = int(input('введи данные массива N'))
arr=[int(input('введи элементы массива arr'))for i in range(N)]
B = int(input('введите номер элемента массива B:'))
C = int(input('ввдете номер элемента массива C:'))

arr [(B - 1 ):C] = []

print('конечный результат',arr)