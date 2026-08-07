class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            # in py to call a functn u have to use .self keyword
            while left < right and not self.isalphnum(s[left]):
                left+=1
            while right > left and not self.isalphnum(s[right]):
                right -= 1 #why decrementing this 
            
            if(s[left].lower() !=s[right].lower() ):
                # not pallindrome
                return False
            left +=1
            right -= 1
        return True
    
    # create alphanum class
    def isalphnum(self,char):
        # three cases - upper lower or digit 
        return ((ord('A')<= ord(char)<= ord('Z')) or 
            (ord('a')<=ord(char)<=ord('z')) or 
            (ord('0')<=ord(char)<=ord('9')))

    '''result = []
                # BRUTE FORCE
            for char in s:
                if char.isalnum(): #removes punctuation + space

                    result.append(char.lower())

            # compare cleaned string with its reverse
            if(result == result[::-1]):
                return True
            else:
                return False'''