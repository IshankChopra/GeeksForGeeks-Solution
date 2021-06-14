#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        l=len(S)
        r=0
        g=0
        for i in S:
            if(i=="R"):
                r=r+1
            else:
                g=g+1
        if(g<r):
            return(l-r)
        else:
            return(l-g)
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
# } Driver Code Ends