class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # logic - every time u see number first push
        # every time u see operator - pop last two elem , perform operation
        # then push res to stack arr
        stack = [] #stack uses LIFO
        for char in tokens:
            # if token in {operators set}:
            if (char == '+' or char == '-' or char == '/' or char == '*'):
                # pop last two elements and perform operation
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b) 
                elif char == '-':
                    stack.append(a - b)
                elif char == '/':
                    stack.append(int(a / b)) 
                else:
                    stack.append(a*b) 
            else:

                # Token is a number → push to stack
                stack.append(int(char))
        return stack[0]
                

