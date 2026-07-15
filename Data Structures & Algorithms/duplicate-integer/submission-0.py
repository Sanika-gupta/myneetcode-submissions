class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = [ 1, 2, 3, 3] #to check if it has duplicate 
        # seenset = {} => a dictionary
        seen = set()
        for i in range(len(nums)):# want every element to be iterated through
            if nums[i] not in seen:
                seen.add(nums[i]) #updating the set 
            elif nums[i] in seen: #it already exists in set and they match
                return True #return true because duplicate 
            
        return False #false because no duplicates 