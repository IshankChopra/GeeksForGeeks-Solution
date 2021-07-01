t=int(input())
def new(A,B,C,D):
    arr=[0]*D
    arr[0]=A
    arr[1]=B
    arr[2]=C
    for i in range(3,D):
        arr[i]=arr[i-1]+arr[i-2]+arr[i-3]

    return(arr[D-1])
for i in range(t):
    a=list(map(int,input().split()))
    A=a[0]
    B=a[1]
    C=a[2]
    D=a[-1]
    print(new(A,B,C,D))



