"""
You are climbing a stair case.
It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""

def climb_stais(n):
    ways=[]
    all_ways()


def all_ways(res,n,n1,sum):
    if sum+1<n:
        n1.append(1)
        all_ways(res,n,n1,sum+1)
    if sum+1==n:
        n1.append(1)
        res.append(n1)
    if sum+2<n:
        n1.append(2)
        all_ways(res,n,n1,sum+2)
    if sum+2==n:
        n1.append(2)
        res.append(n1)
