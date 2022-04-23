a = int(input('введи число '))
b = int(input('введи кратность '))

if a % 2 ==0 and a % b ==0:
	print('число кратное  4')
elif a % 2 !=0 or a % b ==0:
	print('нtчетное или не кратное 4')

if a % 2 == 0 and a % b !=0:
	print('четное и некратное  ') 
elif a % 2 != 0 and a % b !=0:
	print('не четное и не кратное')	