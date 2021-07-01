'''n=int(input())
s=0
for i in range(1,n+1):
    s=s+i
print(s)'''


def rec(n):
    if(n==0):
        return(0)
    else:
        s=n+rec(n-1)
        return(s)

n=int(input())
print(rec(n))