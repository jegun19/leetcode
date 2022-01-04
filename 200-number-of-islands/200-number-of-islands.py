class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= height or j < 0 or j >= width or grid[i][j] == "0":
                return 0
            else:
                grid[i][j] = "0"
                
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)
                
                return 1
        
        height = len(grid)
        if height == 0:
            return 0
        else:
            width = len(grid[0])
            if width == 0:
                return 0
            else:
                numIsland = 0
                
                for i in range(0, height):
                    for j in range(0, width):
                        if grid[i][j] == "1":
                            numIsland += dfs(grid, i, j)
                            
                return numIsland
                        
        return x
        
    