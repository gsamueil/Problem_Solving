class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)
        products=[1]*length
        for i in range(1,length):
            products[i]=products[i-1]*nums[i-1]
            print(products[i])

        right=nums[-1]
        for i in range(length-2,-1,-1):
            products[i]*=right
            right*=nums[i]
        return products
test=Solution()
'''  
1      2      3    4  
-------------------------
-      1      2    6
*      *      *         
24     12     4     -
-------------------------
24  12     8          6



'''
print(test.productExceptSelf((1,2,3,4)))