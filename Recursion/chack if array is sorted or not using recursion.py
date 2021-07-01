def sort(arr):
    n=len(arr)
    if(n==1 or n==0):
        return 1
    else:
        return((arr[0]<arr[1] and sort(arr[1:])))


arr=[1,2,3,10,15]
if(sort(arr)):
    print("array is sorted")
else:
    print("array is not sorted")