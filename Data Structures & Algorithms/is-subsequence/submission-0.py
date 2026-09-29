class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # iterate through every letter in s and check if its in T
        # s = node , t = neetcode
        # order matters
        # o(n) linear time just compare both strings
        i,j=0,0
        # i = string s , j = t str
        while i < len(s) and j < len(t):
            if s[i]== t[j]:
                i+=1
            j+=1
        return True if i == len(s) else False

