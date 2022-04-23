oklad = input(('введи совой оклад'))
procent=int(input('введите % ставку '))
nalog=oklad*procent/100
summa=oklad-nalog
print ("сумма на руки ",summa)
print ("налог:",nalog)