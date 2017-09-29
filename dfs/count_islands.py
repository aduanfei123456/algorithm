"""
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Example 1:
11110
11010
11000
00000
Answer: 1
Example 2:
11000
11000
00100
00011
Answer: 3
"""

def num_islands(grid):
    counter=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                counter+=1
                dfs(grid,i,j)
    return counter
def dfs(grid,i,j):
    if grid[i][j]==1:
        grid[i][j]=-1
        for next in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if next[0]<len(grid) and next[0]>=0 and next[1]<len(grid[0]) and next[1]>=0:
                dfs(grid,next[0],next[1])
#        counter+=1
    else:
        return

grid=[[1,1,0,0,0],
[1,1,1,0,0],
[0,0,1,1,0],
[0,0,0,1,1]]
print(num_islands(grid))