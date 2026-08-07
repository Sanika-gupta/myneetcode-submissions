class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # n =  [1,2,3,4], targ = 7
        # brute force - check every num in the array 
        # two pointers - front & back var - check 1st n last elem then increm forw , decrem back
        forw = 0  #forw incremenets if sum is less than target
        backw = len(numbers)-1 # backw decrement if sum is larger than target
        # as long as forward < backward 
        while forw<backw :
            if(numbers[forw]+numbers[backw]==target):
                return [forw + 1, backw + 1] # for correct indices?
            elif (numbers[forw] + numbers[backw] < target ):
                 forw += 1
            else:
                # if(numbers[forw] + numbers[backw] > target):
                backw -= 1
            
