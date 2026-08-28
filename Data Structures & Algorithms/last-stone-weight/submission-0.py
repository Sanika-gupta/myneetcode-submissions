import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate stones to simulate a max heap using Python's min heap
        for i in range(len(stones)):
            stones[i] = -stones[i]
            # build heap ONCE
        heapq.heapify(stones)
        # Keep smashing while at least 2 stones remain
        while len(stones) >= 2:
            x = heapq.heappop(stones)  # Heaviest - smallest elem in heap
            y = heapq.heappop(stones)  # 2nd heaviest
            if x == y:
                continue  # Both destroyed
            # x < y because x is more negative
            # x - y gives the negative of the remaining weight
            heapq.heappush(stones, x - y)
        # Return the remaining stone's positive weight
        if len(stones) == 1:
            return -heapq.heappop(stones)
        return 0