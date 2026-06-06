class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        rows, cols = len(grid),len(grid[0])
        islands = 0
        visited_lands = set()

        def dfs (r,c):
            if min(r,c) <0  or r >=rows or c >= cols or grid[r][c] == '0':
                return 
            if (r,c) in visited_lands:
                return
            
            visited_lands.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(rows):
            for c in range(cols):
                if grid [r][c] == "1" and (r,c) not in visited_lands:
                    dfs(r,c)
                    islands += 1
                
        return (islands)