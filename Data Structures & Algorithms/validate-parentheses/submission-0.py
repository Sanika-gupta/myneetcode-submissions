class Solution:
    def isValid(self, s: str) -> bool:
        # stack - LIFO
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for char in s:
            if char in pairs:
                # return pairs.values()
                top = stack.pop() if stack else "#"  
                if pairs[char] != top:
                    return False

            else:
                # char is an opening bracket → push
                stack.append(char)
        return not stack

