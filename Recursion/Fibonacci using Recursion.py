def fibo(n):
    if(n==0):
        return(0)
    elif(n==1):
        return(0)
    elif(n==2):
        return(1)
    else:
        s=fibo(n-1)+fibo(n-2)
        return(s)






n=int(input())
print(fibo(n))