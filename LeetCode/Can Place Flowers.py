class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if(n==0):
            return True

        planted = 0

        for i in range(len(flowerbed)):
            leftIsEmpty = (i == 0) or (flowerbed[i-1] == 0)
            rightIsEmpty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

            if(flowerbed[i] == 0 and leftIsEmpty and rightIsEmpty):
                flowerbed[i] = 1
                planted += 1

                if(planted == n):
                    return True

        return False
    