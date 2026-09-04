from typing import List
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        # 1 ->>> LAND
        # 0 =>>> WATER
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        # to count num of isalnds use islands
        islands =0
        def bfs(r, c):
            # ITS ITERATIVE SO WE USE QUEUE
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                # 4 directns
                dirct = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr_r , dr_c in dirct:
                    nr, nc = row + dr_r, col + dr_c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:

                        q.append((nr , nc))
                        visited.add((nr , nc))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # do bfs 
                    bfs(r, c)
                    islands+=1
        return islands