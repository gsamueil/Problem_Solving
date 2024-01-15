"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels="aeiouAEIOU"
        slist= list(s)
        i=0
        j=len(slist)-1
        while (i<j):
            if slist[i] not in vowels :
                i+=1
                continue
            if slist[j] not in vowels:
                j-=1
                continue
            slist[i],slist[j]=slist[j],slist[i]
            i +=1
            j -=1
        return "".join(slist)
        
        