""" 205. Isomorphic Strings """

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.


"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapST, mapTS = {}, {}
        
        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or 
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True
test_case = Solution()
print(test_case.isIsomorphic("foo", "bar"))