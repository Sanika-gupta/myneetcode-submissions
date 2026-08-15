class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result needs to be in list format so
        res = []
        # our arr needs to be sorted so , ALW 2 POINTER RUNDS ON ORDER!!
        nums.sort()
        for i, valu in enumerate(nums):
        # gives you both the index and the actual item from a list, tuple,       or string. You use this when you need the value while looping.
            # we dont wanna use the same value in same position twice
            if i>0 and valu == nums[ i - 1 ]:
                continue # dont wanan resuse the same val
            # two pointer logic
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threesum = valu + nums[left] + nums[right]
                if threesum >  0 :
                    right -=1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([valu , nums[left] , nums[right]])
                    # updt THE POINTERS - IMPT , we only have toupdate one ptr
                    left +=1
                    while(nums[left]==nums[left-1] and left<right):
                         #same val eg on lhs [2,2,0,0,-2,-2]
                         left +=1

        return res


        