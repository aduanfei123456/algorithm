"""
WAP to take one element from each of the array add it to the target sum. Print all those three-element combinations.
/*
A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [1, 2, 2, 2]
target = 7
*/
Result:
[[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 4, 2], [2, 2, 3], [2, 2, 3], [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
"""
def get_three(a,b,c,sum):
    result=[]
    for num in a:
        if num<sum:
            res=get_two(b,c,sum-num)
            for r in res:
                r.append(num)
                result.append(r)
    return result
def get_two(b,c,sum):
    result=[]
    for num in b:
        if num<sum:
            for nc in c:
                if nc==sum-num:
                    result.append([num,nc])
    return result
A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [1, 2, 2, 2]
print(get_three(A,B,C,7))

