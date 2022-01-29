class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        coord = []
        arr_of_area = []
        
        def searchIsland(i, j, coord):
            if grid[i][j] != 0:
                grid[i][j] = 0
                coord.append([i,j])
                
                if i - 1 >= 0 :
                    searchIsland(i-1, j, coord)
                if i + 1 < m:
                    searchIsland(i+1, j, coord)
                if j - 1 >= 0:
                    searchIsland(i, j-1, coord)
                if j + 1 < n:
                    searchIsland(i, j+1, coord)
                
                return coord
                
                
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] != 0:
                    # Start to count area of that island
                    searchIsland(i, j, coord)
                    print(coord)
                    
                    # By this point, finish counting area of an island
                    arr_of_area.append(len(coord))
                    
                    # Return container to empty
                    coord = []
        
        if len(arr_of_area) == 0:
            return 0
        else:
            return max(arr_of_area)