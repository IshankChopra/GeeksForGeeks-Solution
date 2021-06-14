#User function Template for python3
class Solution:
	def balancedNumber(self, N):
        s=str(N)
        l=len(s)
        s1=0
        s2=0
        d=l//2
        for i in range(d):
            s1=s1+int(s[i])
        
        for j in range(d+1,l):
            s2=s2+int(s[j])
        
        if(s1==s2):
            return(1)
        else:
            return(0)
	    
		# your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		N = input ()
		ob = Solution()
		if ob.balancedNumber(N):
			print (1)
		else:
			print (0) 
# } Driver Code Ends