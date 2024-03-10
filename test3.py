#==========
#Вопрос 3:
#==========

"""Решил использовать сортировку вставками, т.к. уже отсортированный массив алгоритм пройдет быстро"""

import array, random

ARR_SIZE = 10
RAND_RANGE = 1000

arr = array.array('i')
for i in range(0, ARR_SIZE):
    arr.append(random.randrange(RAND_RANGE))

print(arr)

def sort(arr):
    for i in range(ARR_SIZE - 1, -2, -1):
        j = i + 1
        while(j < ARR_SIZE - 1 and arr[j] < arr[j + 1]):
            n_temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = n_temp
            j += 1
        
sort(arr)
print(arr)