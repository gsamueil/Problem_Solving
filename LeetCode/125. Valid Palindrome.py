class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=''.join(char for char in s if char.isalnum())
        s=s.lower()
        n=len(s)
        if n==0:
            return True
        else:
            return s==s[::-1]
test=Solution()
print(test.isPalindrome('A man, a plan, a canal: Panama'))