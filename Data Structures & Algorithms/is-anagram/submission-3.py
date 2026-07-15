class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # str s = "heart"
        # str t = "earth"
        # now first check is - length check
        if(len(s) == len(t) ): #only then proceed bc anagrams need to have same len
            #now we know they have same len, now i want to have freq of each char in both str and compare them
            count = {} # use a dictionary to store char + its count, inc it as u iterate thro str s , dec it if it matches in str t 
            for i in range(len(s)): # FIRST STRING
                # get current charaacter
                # s.char[i] = ch - wrong no char
                ch = s[i] 
                if ch in count:
                    count[ch] = count[ch]+1
                else:
                    count[ch] = 1
            for j in range(len(t)):
                #get the curr char
                ch = t[j]
                if ch in count:
                    count[ch] = count[ch] - 1
                else:
                    return False
            for value in count.values():
                if value != 0:
                    return False
        elif len(s) != len(t): # shouldve been on top from begining
            return False
        return True
