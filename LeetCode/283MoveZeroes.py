class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        

        Example 1:

        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """
        l=0
        for r in range (len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return nums
test=Solution()
print('[0, 1, 0, 3, 12]')
print(test.moveZeroes([0,1,0,3,12]))