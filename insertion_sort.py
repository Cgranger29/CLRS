
a = [5,2,4,6,1,3]

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i + 1] = key
    return arr

def insertion_sort_decreasing(arr):
    for j in range(len(arr) - 2, -1,-1):
        key = arr[j]
        i = j+1
        while i <= len(arr) - 1 and arr[i] > key:
            arr[i -1] = arr[i]
            i+=1
        arr[i-1] = key
    return arr
        


# print(insertion_sort(a))
print(insertion_sort_decreasing(a))

