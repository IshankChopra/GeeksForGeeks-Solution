#User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, N):
        if(N==6):
            f=1
        elif(N==2):
            f=5
        elif(N==3):
            f=4
        elif(N==1):
            f=6
        elif(N==5):
            f=2
        else:
            f=3
        return(f)
    	#code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends