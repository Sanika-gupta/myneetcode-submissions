class Solution:
    def scoreOfString(self, s: str) -> int:
        # make use of ord
        res = 0
        for i in range(len(s)-1):
            # a = i
            # b = i + 1
            res += abs(ord(s[i+1])-ord(s[i]))
            # res+=res
            # print(res)
        return res
