#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        c=0
        A="QWERTYUIOPLKJHGFDSAZXCVBNM"
        for i in s:
            if i in A:
                c=c+1
        
        return(c)
        # your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends