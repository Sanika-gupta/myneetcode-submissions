class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE sol
        '''RES = 0
        for l in range(len(heights)):
            for r in range(l+1,len(heights) ):
                area = (r - l) * min(heights[l], heights[r])
                RES = max(RES, area)
        return RES ''' #o(n^2) inefficient code 
        left = 0
        right = len(heights)-1
        res = 0
        while left<right:
            # area stays same formula
            area = (right - left) * min(heights[left], heights[right])
            res = max(res,area)
            # updating left right pointers
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return res

