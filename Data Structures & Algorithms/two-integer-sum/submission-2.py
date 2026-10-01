class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        res = []
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if(nums[i]+nums[j]==target):
                    res.append(i)
                    res.append(j)
                # elif
            return res
        O(N2) solution'''
        # o(n) - hashmap
        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            # check if remaining is in seen
            if remaining in seen:
                return [seen[remaining],i]
            else:
                seen[nums[i]] = i

        