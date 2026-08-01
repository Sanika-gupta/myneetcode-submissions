class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
            # BRUTE FORCE
        for char in s:
            if char.isalnum(): #removes punctuation
                result.append(char.lower())

        # Compare cleaned string with its reverse
        if(result == result[::-1]):
            return True
        else:
            return False
