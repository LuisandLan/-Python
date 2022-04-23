import random
A = random.randint(5.10)
arr=[random.randint(0,90) for i in range (A)]
print(arr)
for i in range(A):
    if arr[i] == 0:
        arr[i] = []
        print(arr)