class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        count, cs, ce = 0, 0, n
        
        while cs <= (n-1)//2:
            count = 0
            while count < (ce-cs)-1:
                #horizontal1
                tmp = matrix[cs][cs]
                for j in range(cs+1,ce):
                    currtmp = matrix[cs][j]
                    matrix[cs][j] = tmp
                    tmp = currtmp
                    
                #print(matrix)
                    
                #vertical1
                for i in range(cs+1,ce):
                    currtmp = matrix[i][ce-1]
                    matrix[i][ce-1] = tmp
                    tmp = currtmp
                    
                    
                #horizontal2
                for j in range(ce-2,cs-1,-1):
                    currtmp = matrix[ce-1][j]
                    matrix[ce-1][j] = tmp
                    tmp = currtmp
                    
                #vertical2
                for i in range(ce-2,cs-1,-1):
                    currtmp = matrix[i][cs]
                    matrix[i][cs] = tmp
                    tmp = currtmp
                
                    
                count+=1 
            
            cs+=1
            ce-=1