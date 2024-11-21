# KHENAFIF Chaima + BENAISSA Faiza

def construire_tas(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        tamisser(array, n, i)

def tamisser(array, n, i):
    father = i
    left_son = 2 * i + 1
    right_son = 2 * i + 2
    root = father 

    if left_son < n and array[left_son] > array[root]:
        root = left_son

    if right_son < n and array[right_son] > array[root]:
        root = right_son

    if root != father:
        array[father], array[root] = array[root], array[father]
        tamisser(array, n, root)

array = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]
construire_tas(array)
print("TAS Max:", array)

result = []
n = len(array)
for i in range(n - 1, -1, -1):  
    result.append(array[0])  
    array[0], array[i] = array[i], array[0]  
    tamisser(array, i, 0)  

print("Result:", result)