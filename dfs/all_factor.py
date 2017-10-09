"""
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations
of its factors.Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Examples:
input: 1
output:
[]
input: 37
output:
[]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
"""
from math import sqrt
def get_factors(n):
    def get_factor(n,i,combi,res):
        while i*i<n:
            if n%i==0:
                res+=[combi+[i,int(n/i)]]
                get_factor(n/i,i,combi+[i],res)
            i+=1
        return res
    return get_factor(n,2,[],[])
print(get_factors(48))