class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     # first solving it using brute force 
        # nums = [3,4,5,6]
        # target = 7
        '''for i in range(nums):
            # 1st iteration 1st will be num[i], next elem will be num[i+1]
            j = num[i+1]
            if (num[i] + j == target):
                return num[i],num[i+1] '''
        # 2  loops one for i index ,, one for j index 
        '''for i in range (len(nums)):
            for j in range(i+1 , len(nums)):
                if (nums[i] + nums[j] == target ):
                    newlist = []       
                    newlist.append(i)  
                    newlist.append(j)  
                    return newlist   '''
        # hashmap
        seen = {} 
        for i in range(len(nums)):
            # num[i]
            compliment = target - nums[i] #compliment stores value not the index
                        # if compliment in nums:
                        #     return [nums.index(nums[i]), nums.index(compliment)] #return num[i] index n compliments' index
                # Check if the partner is already in our clipboard
            if compliment in seen:
                return [seen[compliment], i]  # Return stored index AND current index
            
            # If not, add current number to dictnry for FUTURE partners
            seen[nums[i]] = i   
