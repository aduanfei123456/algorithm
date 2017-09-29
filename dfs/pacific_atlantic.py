# Given an m x n matrix of non-negative integers representing
# the height of each unit cell in a continent,
# the "Pacific ocean" touches the left and top edges of the matrix
# and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right)
# from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the
# Pacific and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:

# Given the following 5x5 matrix:

  # Pacific ~   ~   ~   ~   ~
       # ~  1   2   2   3  (5) *
       # ~  3   2   3  (4) (4) *
       # ~  2   4  (5)  3   1  *
       # ~ (6) (7)  1   4   5  *
       # ~ (5)  1   1   2   4  *
          # *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
# (positions with parentheses in above matrix).
def pacific_atlantic(matrix):
    res=[]
    direction=1
    for i ,row in enumerate(matrix):
        for j,col in enumerate(matrix[i]):
            if dfs(matrix,i,j,1) and dfs(matrix,i,j,-1):
                res.append([i,j])
    return res

def dfs(matrix,i,j,direction):
    result=False
    for next in [[i+direction,j],[i,j+direction]]:
        ni=next[0]
        nj=next[1]
        if ni * nj < 0 or ni >= len(matrix) or nj >= len(matrix[0]):
            return True
        if(matrix[i][j]>=matrix[ni][nj]):
            nr=dfs(matrix,ni,nj,direction)
            result=result or nr
    return result
atalas=   [[1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1] ,
            [6,7,1,4,5],
            [5, 1,1,2 ,4]]
print(pacific_atlantic(atalas))