class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = [-1,0,2,4,6,8], target = 4
        # brute force 
        '''for i in range(len(nums)):
            if( nums[i] == target ):
                print(type(i))
                return int(i) #the index   
        return -1 '''
        
        # optimised using lef, right + middle
        ''' left right middle are all indices'''
        left = 0 #left index end of arr
        right = len(nums) - 1 #right INDEX end of array
        while(left <= right ):
            #search in a valid space
            middle = (left+right)//2 #this is INDEX
            if(nums[middle] == target ):
                return middle
            elif (nums[middle] > target ): 
                # UPDATE YOUR RIGHT
                right = middle - 1
            elif(nums[middle] < target ):
                # update ur left
                left = middle + 1
        return -1


       