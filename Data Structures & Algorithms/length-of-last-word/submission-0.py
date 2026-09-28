class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # use split
        new_arr = s.split()
        return len(new_arr[-1])