from random import randint
N = randint(1,10)
array= [randint(1,10) for i in range(N)]
print(array)
for i in range (len(array)//2):
    t= array[i]
    array[i] = array[len(array)//2+i]
    array[len(array)//2 + i ]=t
print(array)