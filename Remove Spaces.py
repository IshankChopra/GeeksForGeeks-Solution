#User function Template for python3
class Solution:
    def modify(self, s):
        l=[]
        s1=""
        for i in range(len(s)):
            if(s[i]!=" "):
                l.append(s[i])
        
        s1="".join(l)
        return(s1)
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends