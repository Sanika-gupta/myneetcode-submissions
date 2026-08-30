class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Loop through the points.
        Calculate their distances.
        Store them in a list.
        Sort the list from closest to farthest.
        Slice/Grab the first k items to return.
        '''
        res = []
        for x, y in points:
            # calculate the distance..
            # dist = math.sqrt((x-0)+(y-0))
            dist = math.sqrt(x**2 + y**2)
            res.append((dist, [x, y]))
        res.sort()
        # return res[:k]
        return [item[1] for item in res[:k]]
            
