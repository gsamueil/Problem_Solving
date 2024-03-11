class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        l=0
        r=len(height)-1
        while l<r:
            area=(r-l)*min(height[r],height[l])
            print('area = ',area)
            max_area=max(max_area,area)
            print('max_area = ',max_area)

            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
test = Solution()
print('the values on the container is ,[1, 8, 6, 2, 5, 4, 8, 3, 7]')
print('the max area on the container is =',test.maxArea([1,8,6,2,5,4,8,3,7]))
    
        