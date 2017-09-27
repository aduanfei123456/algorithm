"""
Write a function that takes an unsigned integer and
returns the number of ’1' bits it has
(also known as the Hamming weight).
For example, the 32-bit integer ’11' has binary
representation 00000000000000000000000000001011,
so the function should return 3.
T(n)- O(log n)
"""
"""
def count_ones(n):
    iterNum=0b000000000001
    i=12
    counter=0
    while i:
        i-=1
        if iterNum&n:
            counter+=1
        iterNum<<=1
    return counter
"""
def count_ones(n):
    counter=0
    while n:
        counter+=n&1
        n>>=1
    return counter
print(count_ones(7))