class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area= 0
        visited = set()

        def dfs(r , c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            if (r, c) in visited or grid[r][c] == 0:
                return 0        
                # 0 - water so if 0 move 
            if grid[r][c] == 1:
                visited.add((r,c))
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                '''[1, 0]   → down
                    [-1, 0]  → up
                    [0, 1]   → right
                    [0, -1]  → left'''
                area = 1
                for dr, dc in directions:
                    # new cell becomes new...
                        new_r = r + dr
                        new_c = c + dc
                    #  explore that neighboring cell and get its area
                    # so call our dfs
                        area +=dfs(new_r, new_c)
        # max_area = max(max_area,area)
                return area

        
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    area = dfs(r,c)
                    max_area = max(max_area,area)
        return max_area