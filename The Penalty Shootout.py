s="20011001121102"
c=0
l=s[-1]
for i in range(len(s)+1):
    if(s[i]=='2'):
        if(s[i+1])=='1':
            c=c+1
        

print(c)