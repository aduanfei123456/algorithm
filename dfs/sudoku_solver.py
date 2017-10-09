"""It's similar to how human solve Sudoku.
create a hash table (dictionary) val to store possible values in every location.
Each time, start from the location with fewest possible values, choose one value
from it and then update the board and possible values at other locations.
If this update is valid, keep solving (DFS). If this update is invalid (leaving
zero possible values at some locations) or this value doesn't lead to the
solution, undo the updates and then choose the next value.
Since we calculated val at the beginning and start filling the board from the
location with fewest possible values, the amount of calculation and thus the
runtime can be significantly reduced:
The run time is 48-68 ms on LeetCode OJ, which seems to be among the fastest
python solutions here.
The PossibleVals function may be further simplified/optimized, but it works just
fine for now. (it would look less lengthy if we are allowed to use numpy array
for the board lol).
"""
def PossibleVal(board):
    a='1234'
    d,val={},{}
    for i in range(4):
        for j in range(4):
            ele=board[i][j]
            if board[i][j]!='.':
                d[("r", i)] = d.get(("r", i), []) + [ele]
                d[("c", j)] = d.get(("c", j), []) + [ele]

            else:
                val[(i,j)]=[]
    for i,j in val.keys():

        npv=d.get(("r", i), [])+d.get(("c",j),[])
        val[(i,j)]+=[int(n) for n in a if int(n) not in npv]

    return val
def TryUpdate(board,res=[]):
    proper=True
    val=PossibleVal(board)
    print(val)
    if not val :
        return True
    LeaCoup=[]
    for key in val.keys():
        LeaCoup=key if ((not LeaCoup) or len(val[key])<len(val[LeaCoup]))else LeaCoup
    if len(val[LeaCoup])==0:
        return False
    possval=val[LeaCoup]
    i,j=LeaCoup
    print(possval)
    for val in possval:
        board[i][j]=val
        proper=proper and TryUpdate(board,res)
        if proper:
            res+=[(i,j,val)]
            return True
        else:
            board[i][j]='.'
    return True

board=[[1,2,3,4],[3,4,1,2],[2,3,4,'.'],[4,1,2,3]]
res=[]
TryUpdate(board,res)
print(res)










