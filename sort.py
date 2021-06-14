l=[5,4,3,2,1]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)

for k in range(0,len(l)-1,2):
    l[k],l[k+1]=l[k+1],l[k]

print(l)