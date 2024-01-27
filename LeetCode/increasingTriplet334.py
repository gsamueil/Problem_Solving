import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1,n2=sys.maxsize,sys.maxsize
        print(nums)

        for n in nums:
            if (n>n2) :
                print(n2)
                return True
            if(n<=n1):
                n1=n
                # print('================')

                print(n1)
            elif(n<=n2):
                n2=n
                print('================')
                print(n)
        return False
test=Solution()
'''
n1      n2      n3   
    <         <
 7
 1 is less the currnt n1 
 1
 2 is not less than or qual n1 then will assigned to n2
        2 
        0 is less than the current n1 then will assign to n1
        3 is greater than n2 then will assign to n3 then return for all True 
           
    
     
 7   1  2  0  3
'''
print(test.increasingTriplet([7,1,2,0,3]))