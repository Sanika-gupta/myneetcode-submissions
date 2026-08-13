class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # iterate through nums for i check if i exists in nums
        # if i exists in array move to next number in array 
        # for each number x in nums:
        #     count how many times x appears in nums
        #     if count == 1:
        #         return x
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range( len(nums)):
        #         if(nums[i]==nums[j]):
        #             count+=1
        #     if count == 1:
        #         return nums[i]
        # xor method
        res = 0 # n xor 0 = n


        for i in nums:
            res = i ^ res
        return res
            


        