
def power(n,p):
    if(p==0):
        return(1)
    else:
        p=n*power(n,p-1)
        return(p)



n=int(input("enter base:"))
p=int(input("enter exponential value:"))
print(power(n,p))
