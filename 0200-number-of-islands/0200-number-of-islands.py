class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dp = [[False for i in range(len(grid[j]))] for j in range(len(grid))]
        count = 0
        
        
        def numIslandsHelp(grid,i,j):
            
            if i<0 or j<0:
                return
            
            if i>=len(grid) or j>=len(grid[i]):
                return
            
            if grid[i][j] == '0' or dp[i][j] is True:
                return 

                        
            dp[i][j] = True
            numIslandsHelp(grid,i+1,j)
            numIslandsHelp(grid,i,j+1)
            numIslandsHelp(grid,i-1,j)
            numIslandsHelp(grid,i,j-1)
                        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if dp[i][j] is False and grid[i][j] == '1':
                    numIslandsHelp(grid,i,j)
                    count+=1
                    
        return count
                        
        
                        
                    
                    
                