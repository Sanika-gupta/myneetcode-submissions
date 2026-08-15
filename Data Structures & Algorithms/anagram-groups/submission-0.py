from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop"]
        # output - [ ["act", "cat"],["stop", "pots", "tops"] ]
        # creating empty  DEFAULT DICT dictionary - which will store key,value 
        anagram_dict = defaultdict(list)
        for st in strs:
            count = [0] * 26
            # for each char in one str
            for char in st:
                count[ord(char)-ord('a')]+=1
                # bump up the count at each letter that exists in str 
                # makes the arr go from - count[0...0] -> count[1...0]
            key = tuple(count) #tuple to make it hashable / immutable 
            anagram_dict[key].append(st)
        return list(anagram_dict.values())