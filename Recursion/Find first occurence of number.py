def first_occur(arr, i, n, key):
    if i == n:
        return -1
    if arr[i] == key:
        return i
    else:
        return first_occur(arr, i + 1, n, key)


arr = [4, 2, 1, 2, 5, 2, 7]
n = len(arr)
key = 4
print(first_occur(arr, 0, n, key))
