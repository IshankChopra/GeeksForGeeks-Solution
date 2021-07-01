a="amazon"
b=[]
f=a[0]

for i in range(len(a)-1,1,-1):
    b[i]=b[i-1]

print(b)

