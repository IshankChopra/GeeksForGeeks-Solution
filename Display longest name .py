#User function Template for python3

class Solution:
    def longest(self, names, n):
        ma=-1


        for i in range(len(names)):
          if(len(names[i])>ma):
            ma=len(names[i])
            res=names[i]
        return(res)
        
    	# code here
    	
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends